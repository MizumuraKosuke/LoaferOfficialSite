var cnt = 0;

var timer1;

function slideNews(){
    cnt++;
    if (cnt >= current) {
        cnt = 0;
    }
    document.getElementById("hnp").src = image[cnt].src;
    document.getElementById("hnt").innerHTML = title[cnt];
    timer1 = setTimeout("slideNews()",5000);
}

function forwardNews(){
    clearTimeout(timer1);
    cnt++;
    if (cnt >= current) {
        cnt = 0;
    }
    document.getElementById("hnp").src = image[cnt].src;
    document.getElementById("hnt").innerHTML = title[cnt];
    timer1 = setTimeout("slideNews()",5000);
}

function backNews(){
    clearTimeout(timer1);
    cnt--;
    if (cnt < 0) {
        cnt = current-1;
    }
    document.getElementById("hnp").src = image[cnt].src;
    document.getElementById("hnt").innerHTML = title[cnt];
    timer1 = setTimeout("slideNews()",5000);
}

slideNews();