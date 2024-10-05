import os
import warnings

import discord
import fastf1.plotting
from discord.ext import commands
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib import cm
import seaborn as sns
from datetime import datetime
import csv
from pytz import timezone

from embed import F1Embed

warnings.filterwarnings('ignore')
intents = discord.Intents.default()
intents.message_content = True
fastf1.plotting.setup_mpl(misc_mpl_mods=False)

bot = commands.Bot(command_prefix='+', intents=intents)


class F1Event:
    def __init__(self, race_name, event_type, start_time, location, country):
        self.race_name = race_name
        self.event_type = event_type
        self.start_time = start_time
        self.location = location
        self.country = country


def f1events():
    f1_list = []
    with open('sched.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            country = row[0]
            location = row[1]
            race_name = row[2]

            i = 3
            while i <= 12:
                event_type = row[i]
                start_time = datetime.strptime(row[i + 1], '%Y-%m-%d %H:%M:%S')
                f1_list.append(F1Event(race_name, event_type, start_time, location, country))
                i += 2
    return f1_list

f1_events= f1events()


@bot.command()
async def f1(ctx):
    global f1_events  # Use the globally initialized f1_events list

    current_time = datetime.utcnow()

    # Remove past events from the f1_events list
    f1_events = [event for event in f1_events if event.start_time > current_time]

    if not f1_events:
        await ctx.send(
            "No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to the event date."
        )
        return

    # Get the first upcoming event
    next_event = f1_events[0]

    # Create the embed using the F1Embed class
    f1_embed = F1Embed(next_event)
    embed_message = f1_embed.create_embed()

    # Send the embed in the channel
    await ctx.send(embed=embed_message)

@bot.command()
async def speedtrace(ctx, arg1, arg2, arg3, arg4, arg5):
    await ctx.send("FastF1 can take up to 30s to fetch data for a race unless it is already cached."
                   " Stand by, your graph will be loaded shortly.")

    year = int(arg1)
    race = arg2
    event = arg3
    driver1 = arg4
    driver2 = arg5

    session = fastf1.get_session(year, race, event)
    session.load()

    driver1_lap = session.laps.pick_driver(driver1).pick_fastest()
    driver2_lap = session.laps.pick_driver(driver2).pick_fastest()
    fastest_lap = session.laps.pick_fastest()
    car_data = fastest_lap.get_car_data().add_distance()
    circuit_info = session.get_circuit_info()
    v_min = car_data['Speed'].min()
    v_max = car_data['Speed'].max()

    driver1_tel = driver1_lap.get_car_data().add_distance()
    driver2_tel = driver2_lap.get_car_data().add_distance()

    driver1_color = fastf1.plotting.driver_color(driver1)

    driver2_color = fastf1.plotting.driver_color(driver2)

    fig, ax = plt.subplots()
    ax.plot(driver1_tel['Distance'], driver1_tel['Speed'], color=driver1_color, label=driver1)
    ax.plot(driver2_tel['Distance'], driver2_tel['Speed'], color=driver2_color, label=driver2)
    ax.vlines(x=circuit_info.corners['Distance'], ymin=v_min - 20, ymax=v_max + 20,
              linestyles='dotted', colors='grey')
    for _, corner in circuit_info.corners.iterrows():
        txt = f"{corner['Number']}{corner['Letter']}"
        ax.text(corner['Distance'], v_min - 30, txt,
                va='center_baseline', ha='center', size='small')

    ax.set_xlabel('Distance in m')
    ax.set_ylabel('Speed in km/h')
    ax.set_ylim([v_min - 40, v_max + 20])
    ax.legend()
    plt.suptitle(f"Fastest Lap Comparison \n "
                 f"{session.event['EventName']} {session.event.year} ")
    filename = "plot.png"
    plt.savefig(filename)
    image = discord.File(filename)

    await ctx.send(file=image)

    plt.close()


@bot.command()
async def gearshifts(ctx, arg1, arg2, arg3, arg4):
    session = fastf1.get_session(int(arg1), arg2, arg3)
    session.load()

    lap = session.laps.pick_driver(arg4).pick_fastest()

    tel = lap.get_telemetry()

    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    gear = tel['nGear'].to_numpy().astype(float)

    cmap = cm.get_cmap('Paired')
    lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N + 1), cmap=cmap)
    lc_comp.set_array(gear)
    lc_comp.set_linewidth(4)

    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    plt.suptitle(
        f"Fastest Lap Gear Shift Visualization\n"
        f"{lap['Driver']} - {session.event['EventName']} {session.event.year}"
    )

    cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
    cbar.set_ticks(np.arange(1.5, 9.5))
    cbar.set_ticklabels(np.arange(1, 9))
    filename = "plot.png"
    plt.savefig(filename)
    image = discord.File(filename)

    await ctx.send(file=image)

    plt.close()


@bot.command()
async def racepace(ctx, arg1, arg2):
    fastf1.plotting.setup_mpl(mpl_timedelta_support=False)
    year = int(arg1)
    race = fastf1.get_session(year, arg2, 'R')
    race.load()

    point_finishers = race.drivers[:10]
    print(point_finishers)
    driver_laps = race.laps.pick_drivers(point_finishers).pick_quicklaps()
    driver_laps = driver_laps.reset_index()

    finishing_order = [race.get_driver(i)["Abbreviation"] for i in point_finishers]
    print(finishing_order)

    driver_colors = {abv: fastf1.plotting.DRIVER_COLORS[driver] for abv,
    driver in fastf1.plotting.DRIVER_TRANSLATE.items()}
    print(driver_colors)

    fig, ax = plt.subplots(figsize=(10, 5))

    driver_laps["LapTime(s)"] = driver_laps["LapTime"].dt.total_seconds()

    sns.violinplot(data=driver_laps,
                   x="Driver",
                   y="LapTime(s)",
                   inner=None,
                   scale='area',
                   order=finishing_order,
                   palette=driver_colors
                   )

    sns.swarmplot(data=driver_laps,
                  x="Driver",
                  y="LapTime(s)",
                  order=finishing_order,
                  hue="Compound",
                  palette=fastf1.plotting.COMPOUND_COLORS,
                  hue_order=["SOFT", "MEDIUM", "HARD"],
                  linewidth=0,
                  size=5
                  )

    ax.set_xlabel("Driver")
    ax.set_ylabel("Lap Time (s)")
    plt.suptitle(f"Race Pace Comparison \n "
                 f"{race.event['EventName']} {race.event.year} ")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    filename = "plot.png"
    plt.savefig(filename)
    image = discord.File(filename)

    await ctx.send(file=image)

    plt.close()


@bot.command()
async def teampace(ctx, arg1, arg2):
    race = fastf1.get_session(int(arg1), arg2, 'R')
    race.load()
    laps = race.laps.pick_quicklaps()

    ###############################################################################
    # Convert the lap time column from timedelta to integer.
    # This is a seaborn-specific modification.
    # If plotting with matplotlib, set mpl_timedelta_support to true
    # with plotting.setup_mpl.
    transformed_laps = laps.copy()
    transformed_laps.loc[:, "LapTime (s)"] = laps["LapTime"].dt.total_seconds()

    # order the team from the fastest (lowest median lap time) tp slower
    team_order = (
        transformed_laps[["Team", "LapTime (s)"]]
        .groupby("Team")
        .median()["LapTime (s)"]
        .sort_values()
        .index
    )
    print(team_order)

    # make a color palette associating team names to hex codes
    team_palette = {team: fastf1.plotting.team_color(team) for team in team_order}

    ###############################################################################
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.boxplot(
        data=transformed_laps,
        x="Team",
        y="LapTime (s)",
        order=team_order,
        palette=team_palette,
        whiskerprops=dict(color="white"),
        boxprops=dict(edgecolor="white"),
        medianprops=dict(color="grey"),
        capprops=dict(color="white"),
    )

    plt.title(f"Race Pace Visualization\n"
              f"{race.event['EventName']} {race.event.year}")
    plt.grid(visible=False)

    # x-label is redundant
    ax.set(xlabel=None)
    plt.tight_layout()
    filename = "plot.png"
    plt.savefig(filename)
    image = discord.File(filename)

    await ctx.send(file=image)

    plt.close()


@bot.command()
async def hi(ctx, arg):
    await ctx.send(arg)


token = os.getenv('token')
bot.run(token)
