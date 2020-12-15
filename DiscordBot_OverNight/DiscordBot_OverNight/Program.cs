using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System;
using System.Threading.Tasks;

namespace DiscordBot_OverNight
{
    class Program
    {
        //Client: 봇 클라이언트 || commands: 명령어 수신 클라이언트
        DiscordSocketClient client;
        CommandService commands;

        // 프로그램 진입점
        static void Main(string[] args)
        {
            new Program().BotMain().GetAwaiter().GetResult();               //봇 진입점 실행
        }

        // 봇 진입점
        public async Task BotMain()
        {
            client = new DiscordSocketClient(new DiscordSocketConfig()
            {
                LogLevel = LogSeverity.Verbose  //봇 로그 레벨 설정
            }); //봇 클라 초기화
            commands = new CommandService(new CommandServiceConfig()
            {
                LogLevel = LogSeverity.Verbose  //봇 로그 레벨 설정
            }); //명령어수신 client

            //로그 수신시 출력 함수에서 출력
            client.Log += OnClientLogReceived;
            commands.Log += OnClientLogReceived;

            //토큰 사용 로그인 -> 이벤트 수신 시작
            await client.LoginAsync(TokenType.Bot, "Nzg4MzgzOTE5OTA0MzkxMTkz.X9itvQ.YAIb0kvOK3mRlFly8NKK44hoO8s");
            await client.StartAsync();

            client.MessageReceived += OnClientMessage;      //메세지 수신 처리

            await Task.Delay(-1);       //봇 종료 방지 딜레이 추가
        }
        public async Task OnClientMessage(SocketMessage arg)
        {
            //수신한 메시지가 사용자가 보낸게 아닌 경우 취소
            var message = arg as SocketUserMessage;
            if (message == null) return;

            int pos = 0;

            //메시지 앞에 !없음 + 타 봇 호출시 => 취소
            if (!(message.HasCharPrefix('!', ref pos) ||
                message.HasMentionPrefix(client.CurrentUser, ref pos)) ||
                message.Author.IsBot)
                return;

            /*
            //수신 메시지에 대한 context 생성 => 수신 명령어 다시 보냄
            var context = new SocketCommandContext(client, message);
            await context.Channel.SendMessageAsync("Receive command: " + message.Content);
            */

            if (message.Content == "!무작위")
            {
                Random rand_tmpInt = new Random();
                string rand_tmpStr = rand_tmpInt.Next(1, 10).ToString();

                var context = new SocketCommandContext(client, message);
                await context.Channel.SendMessageAsync("무작위 명령: " + rand_tmpStr);
            }
        }

        //봇 로그 출력
        private Task OnClientLogReceived(LogMessage msg)
        {
            Console.WriteLine(msg.ToString());  //로그 출력
            return Task.CompletedTask;
        }
    }
}
