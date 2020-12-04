const puppeteer = require('puppeteer');

async function scrapeChannel(url) {

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto(url);


    const [el] = await page.$x('/html/body / section / section / h1 / span / span[1]');
    const text = await el.getProperty('textContent');
    const name = await text.jsonValue();

    const [el2] = await page.$x('/html/body/section/section/section/figure/div[1]/div/div/div[3]/picture/img');
    const src = await el2.getProperty('src');
    const imgURL = await src.jsonValue();

    browser.close();

    console.log({name, imgURL})

    return {name}
    
}

scrapeChannel("https://houston.craigslist.org/fod/d/humble-seat-spyder-200-go-kart/7240809292.html")