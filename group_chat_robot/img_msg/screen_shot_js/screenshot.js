


const puppeteer = require('puppeteer');
const program = require('commander');


/**
 * 运行参考：
 *node screenshot.js -u https://www.baidu.com/ -s #lg -p toc.jpg
 */

program.option('-u, --url [type]', 'url address')
    .option('-s, --selector [type]', 'selector')
    .option('-p, --path [type]', 'shot path')
    .parse(process.argv);

// 参数校验
let url = 'http://javascript.ruanyifeng.com/nodejs/packagejson.html';
let selector = '#toc';
let path = '/tmp/table.jpg';
if (program.url && program.path != true) {
    console.log(program.url);
    url = program.url;
} else {
    console.log("请输入网址参数 -u 'http://xxx'");
    process.exit();
}

if (program.selector && program.path != true) {
    console.log(program.selector);
    selector = program.selector;
} else {
    console.log("请输入元素选择器参数 -s 'x | .x | #x'");
    process.exit();
}

if (program.path && program.path != true) {
    console.log(program.path);
    path = program.path;
}
else {
    console.log("请输入保存路径参数 -p '/tmp/x.jpg'");
    process.exit();
}

puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    headless: true
    // executablePath: 'D:\\ProgramFiles\\Python36\\Scripts\\chromedriver.exe'
}).then(async browser => {
    try {
        const page = await browser.newPage();
        await page.setViewport({width: 2560, height: 1000});
        await page.goto(url);
        console.log("加载网页...");
        await sleep(5000);
        await page.waitFor(selector);
        let table = await page.$(selector);
        if (!table) {
            console.log(selector + " 没有找到该元素");
            await browser.close();
            process.exit();
        }
        let viewport = page.viewport();
        let clip = await table.boundingBox();
        viewport['height'] = parseInt(clip['y'] + clip['height']) + 10;
        await page.setViewport(viewport);
        console.log("图片截取中...");
        await table.screenshot({
            path: path,
            clip: clip,
            quality: 100
        });
        console.log("截取成功");
    }catch (error){
        console.log("截取失败");
        console.log(error);
    }
    await browser.close();

});

// sleep 以等待网页加载
async function sleep(ms) {
    await new Promise(resolve => setTimeout(resolve, ms))
}
