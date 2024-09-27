import TelegramBot from "node-telegram-bot-api";

const token = '7272572787:AAGIYaDNqRR3DNUwvqM9Npvv-w73dsILp18'

const bot = new TelegramBot(token, { polling: true })



bot.on('message',(msg)=>{
    const chatId = msg.chat.id
    bot.sendMessage(chatId,'Hello I am your Bot')
})

bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Welcome! Use /help to see available commands.');
});