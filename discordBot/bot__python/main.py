import discord
import youtube_dl
import spotify
from discord.ext import commands
from discord.utils import get
import random
import os
import shutil

val_token = 'Token'
bot = commands.Bot(command_prefix='#')
db_youtubeQueue={}
db_musicName=[]

'''
발견된 에러
1. queue에서 제거시 len(queue)와 파일명 사이에서 이름 중복 충돌 발생
2. def 내에서 await를 통한 send가 불가능함
보완점
1. 시작/종료 시 음악 전체 초기화
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name="t_ping")
async def test_CheckPing(ctx):
    print(f'Bot Status: Now ping {round(bot.latency*1000)}ms')

@bot.command(name="join", pass_context=True)
async def status_join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        await ctx.send(f"[오류] 이미 봇이 다른 채널에서 노래를 재생하고 있습니다.")
        return

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"Bot Status: connect {channel}")
    await ctx.send(f"봇이 {channel} 채널에 참여했습니다.")

@bot.command(name="leave", pass_context=True)
async def status_leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Bot Status: leave {channel}")
        await ctx.send(f"봇이 {channel} 채널을 떠났습니다.")
    else:
        await ctx.send("[오류] 봇이 이미 채널을 떠난 상태입니다.")

@bot.command(name="유튜브", pass_context=True)
async def youtube_play(ctx, url: str):
    def chk_queue():
        queue_infile = os.path.isdir("./queue")
        if queue_infile is True:
            dir = os.path.abspath(os.path.realpath("queue"))
            length = len(os.listdir(dir))
            print(length)
            still_q = length - 1
            try:
                first_file = os.listdir(dir)[0]
            except:
                print("No more queued songs")
                db_youtubeQueue.clear()
                return
            main_loc = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("queue") + "\\" + first_file)

            if length != 0:
                print("Bot Status: Playing next queued")
                print(f"Bot Status: {still_q} song(s) still exist")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_loc)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                #ctx.send(f":headphones:현재 재생중 : {db_musicName[0]}")
                print(f"Bot Status: Now playing {db_musicName[0]}")
                db_musicName.pop(0)

                voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: chk_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.5
            else:
                db_youtubeQueue.clear()
                return
        else:
            db_youtubeQueue.clear()
            print("Bot Status: No songs are exist in queue")

    voice = get(bot.voice_clients, guild=ctx.guild)
    if not(voice and voice.is_connected()):
        await ctx.send("[오류] 현재 봇이 보이스채널에 참여하지 않았습니다.")
        return

    song_exist = os.path.isfile("song.mp3")
    try:
        if song_exist:
            os.remove("song.mp3")
            db_youtubeQueue.clear()
    except PermissionError:
        await ctx.send("노래가 이미 재생중입니다!")
        return

    queue_infile = os.path.isdir("./queue")
    try:
        queue_folder = "./queue"
        if queue_infile is True:
            print("Bot Status: Remove old queue folder")
            shutil.rmtree(queue_folder)
    except:
        print("No old queue folder")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet' : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Bot Status: Downloading audio")
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Bot Status: {file} renamed")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: chk_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.5

    nname = name.rpartition("-")
    await ctx.send(f":headphones:현재 재생중 : {nname[0]}")
    print(f"Bot Status: Now playing {nname[0]}")

@bot.command(name="정지", pass_context=True)
async def youtube_pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        await ctx.send("[오류] 현재 음악이 일시정지 중 입니다.")
        return
    if voice and voice.is_playing():
        print("Bot Status: Music passed")
        voice.pause()
        await ctx.send("음악을 일시정지합니다.")
    else:
        await ctx.send("[오류] 음악 재생중이 아닙니다.")
@bot.command(name="재개", pass_context=True)
async def youtube_resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        await ctx.send("[오류] 노래가 이미 재생중입니다.")
        return
    if voice and voice.is_paused():
        print("Bot Status: Music resumed")
        voice.resume()
        await ctx.send("음악을 다시 재생합니다.")
    else:
        await ctx.send("[오류] 음악 재생중이 아닙니다.")
@bot.command(name="스킵", pass_context=True)
async def youtube_stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    db_youtubeQueue.clear()

    if voice and voice.is_playing():
        print("Bot Status: Music Skipped")
        voice.stop()
        await ctx.send("현재 음악을 스킵합니다.")
    else:
        await ctx.send("[오류] 음악 재생중이 아닙니다.")

@bot.command(name="queue", pass_context=True)
async def youtube_queue(ctx, url: str):
    queue_infile = os.path.isdir("./queue")
    if queue_infile is False:
        os.mkdir("queue")
    dir = os.path.abspath(os.path.realpath("queue"))
    queue_num = len(os.listdir(dir))
    queue_num += 1
    add_queue = True
    while add_queue:
        if queue_num in db_youtubeQueue:
            queue_num += 1
        else:
            add_queue = False
            db_youtubeQueue[queue_num] = queue_num

    dir_queue = os.path.abspath(os.path.realpath("queue") + '/%(title)s.%(ext)s')
    #dir_queue = os.path.abspath(os.path.realpath("queue") + f"\song{queue_num}.%(ext)s")
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl' : dir_queue,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Bot Status: Downloading audio")
        ydl.download([url])
    for file in os.listdir("./queue"):
        if file.endswith(".mp3"):
            name = file
            print(f"Bot Status: {file} renamed")
            os.rename(os.path.join("./queue", file), os.path.join("./queue", f"song{queue_num}.mp3"))
    nname = name.rpartition(".")
    db_musicName.append(nname[0])

    await ctx.send(f"노래 추가: {nname[0]}\n노래 대기 현황: " + str(queue_num))
    print(f"Bot Status: {nname[0]} song added")

@bot.command(name="명령어")
async def print_taskInformation(ctx):
    str_task="@@@@@명령어 리스트@@@@@\n#주사위 x / #주사위 x y : 1~x,x~y 사이의 임의값을 출력합니다.\n#선택 a b ... : 주어진 단어 중 하나를 선택합니다."
    await ctx.send(str_task)

@bot.command(name="주사위")
async def print_roll(ctx,*args):
    if len(args)==0:
        await ctx.send('[오류] 값이 존재하지 않습니다.')
        return
    if len(args)>=3:
        await ctx.send('[오류] 값이 너무 많습니다.')
        return
    try:
        val_st=int(args[0])
        if len(args)>1:val_ed=int(args[1])
        else:val_ed=1
    except Exception:
        await ctx.send('[오류] 잘못된 값입니다.')
        return

    if val_st>val_ed:val_st,val_ed=val_ed,val_st
    await ctx.send(f"주사위: {random.randint(val_st, val_ed)}")
@bot.command(name="선택")
async def print_selectRandom(ctx,*args):
    if len(args)==0:
        await ctx.send('[오류] 값이 존재하지 않습니다')
        return
    if len(args)>10:
        await ctx.send('[오류] 값이 너무 많습니다.')
        return

    idx = random.randint(0, len(args)-1)
    await ctx.send(f"선택: {args[idx]} ")

bot.run(val_token)