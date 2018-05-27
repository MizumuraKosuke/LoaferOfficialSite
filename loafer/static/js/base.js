/*var image = new Array();

image[0] = new Image();
image[0].src = "/../static/media/news/image.png";
image[1] = new Image();
image[1].src = "/../static/media/news/image-2.png";
*/

var cnt = 0;

var timer1;

function slideNews(){
    cnt++;
    if (cnt >= current) {
        cnt = 0;
    }
    document.getElementById("sd").src = image[cnt].src;
    timer1 = setTimeout("slideNews()",5000);
}

function forwardNews(){
    clearTimeout(timer1);
    cnt++;
    if (cnt >= current) {
        cnt = 0;
    }
    document.getElementById("sd").src = image[cnt].src;
    timer1 = setTimeout("slideNews()",5000);
}

function backNews(){
    clearTimeout(timer1);
    cnt--;
    if (cnt < 0) {
        cnt = current-1;
    }
    document.getElementById("sd").src = image[cnt].src;
    timer1 = setTimeout("slideNews()",5000);
}

slideNews();