// Express кітапханасын қосу
const express = require('express');
const app = express();

// Негізгі маршрут
app.get('/', (req, res) => {
    res.send('Қош келдіңіз! Бұл Балқиямен құрылған Node.js және Express.js сервері.');
});

// Басқа маршрут
app.get('/about', (req, res) => {
    res.send('Бұл сервер туралы Балқияның ақпарат беті.');
});

app.get('/balkiya', (req, res) => {
    res.send('Salem. kalaisyn?')
})

// Логгер орта қабаты
app.use((req, res, next) => {
    console.log(`${req.method} сұранысы ${req.url} мекенжайына жіберілді.`);
    next();
});

// Асинхронный маршрут
app.get('/async', async (req, res) => {
    const data = await getDataFromDB(); // Қолданылуы мысал ретінде
    res.send('Асинхронды маршруттың деректері: ' + data);
});

async function getDataFromDB() {
    return 'Асинхронды деректер';
}

// Серверді тыңдау үшін портты орнату
const port = 19505;
app.listen(port, () => {
    console.log(`Сервер ${port}-портта жұмыс істеп тұр.`);
});
