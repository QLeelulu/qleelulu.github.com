!SLIDE

# HTML5 & CSS3
## <font color="#666">in</font>
# FaWave

!SLIDE

# 说些什么？

> 1. FaWave使用到的HTML5与CSS3
>
> 2. 多为普通web开发用到的
>
> 4. 不会太深入技术细节
>
> 3. 不讨论浏览器兼容性和平台差异性

!SLIDE

# 等等，
# 什么是FaWave ?

!SLIDE

# CSS3

+ ### 圆角
+ ### 阴影
+ ### 动画
+ ### 布局
+ ### and more

!NOTES

# You can even include notes

!SLIDE

# CSS3 圆角  
<br/>

@@@ css
    .radius {
        border-radius: 50px;
	    border-top-right-radius: 3px 3px;
    }
@@@

<span class="sample radius"></span>

!SLIDE

# CSS3  阴影
<br/>

@@@ css
    .shadow {
        box-shadow: 10px 10px 15px rgba(0,0,0, .5);
        text-shadow: 0 0 4px white, 
            0    -5px  4px  rgb(255, 255, 51), 
            2px  -10px 6px  rgb(255, 221, 51), 
            -2px -15px 11px rgb(255, 136, 0), 
            2px  -25px 18px rgb(255, 34, 0);
    }
@@@

<span class="sample shadow">FaWave Is Cool</span>

!SLIDE

# CSS3 渐变
<br/>

@@@ css
    .linear-gradient {
        background: -webkit-linear-gradient(
            left, 
            red, orange, yellow, green, blue
        );
    }
@@@

<span class="sample linear-gradient"></span>

!SLIDE

# CSS3 动画
<br/>

@@@ css
    .transition{
        -webkit-transition: all 0.8s ease;
    }
    .transition:hover{
        background: #5CC04F;
        color: #fff;
        box-shadow: rgba(0, 0, 0, 0.5) 10px 10px 20px;
    }
@@@

<span class="sample transition">鼠标移上来看看</span>

!SLIDE

# CSS3用在FaWave哪些地方了？

!SLIDE

!SLIDE

# HTML5

<br/>

推荐阅读这篇文章： [HTML5设计原理](http://www.cn-cuckoo.com/2010/10/21/the-design-of-html5-2151.html)

!SLIDE

# FaWave用到哪些HTML5的特性

+ ### Local Storage
+ ### 地理定位
+ ### Ajax 文件上传
+ ### Canvas
+ ### Audio
+ ### 桌面提醒
+ ### and more ?

!SLIDE

# Local Storage

@@@ js
    Storage.prototype.setObject = function(key, value) {
        this.setItem(key, JSON.stringify(value));
    };

    Storage.prototype.getObject = function(key) {
        var v = this.getItem(key);
        if(v){
            try{
                v = JSON.parse(v);
            }catch(err){ }
        }
        return v;
    };
@@@

!SLIDE

# Geolocation

@@@ js
    if(navigator.geolocation){
        navigator.geolocation
                 .getCurrentPosition(function(position){
            var p = {latitude: position.coords.latitude, 
                     longitude: position.coords.longitude};
            //Map.show(p);
        }, function(errorMsg){
        });
    }else{
        alert('Sorry, geolocation services are not supported by your browser!');
    }
@@@

!SLIDE

# 图片预览

@@@ js
    var reader = new FileReader(),
        file = $("input:file").get(0).files[0];
    reader.onload = function(e){
        $("#imgPreview")
          .html('<img src="' + e.target.result + '" />');
    };
    reader.readAsDataURL(file);
@@@

!SLIDE

# 粘帖图片

@@@ js
    window.document.onpaste = function(e){
        var f = null,
            items = e.clipboardData &&
				    e.clipboardData.items;
        items = items || [];
		for(var i=0; i<items.length; i++){
            if(items[i].kind === 'file'){
                f = items[i].getAsFile();
                break;
            }
        }
        if(f){ /* do anything you want */ }
    };
@@@

!SLIDE

# 纯AJAX文件上传

@@@ js
    var file = $("input:file").get(0).files[0];
    $.ajax({
        data: file,
        contentType: file.fileType || file.type,
        xhr: xhr_provider(onprogress),
        url: "url",
        type: "post",
        processData: false,
        success: function(result) {
        }
    });
@@@

!SLIDE

@@@ js
    var xhr_provider = function(onprogress) {
        return function() {
            var xhr = jQuery.ajaxSettings.xhr();
            if(onprogress && xhr.upload) {
                xhr.upload
                   .addEventListener('progress', 
                        onprogress, false);
            }
            return xhr;
        };
    };
@@@

!SLIDE

# Audio
#### 新微博声音提醒
<br/>

@@@ js
    var audio = new Audio();
    audio.src = 'alert.mp3';
    audio.play();
@@@

!SLIDE

# 桌面提醒 [<a href="javascript:" onclick="notification()" style="color:#ccc">点我看看</a>]

@@@ js
    function RequestPermission (callback){
        window.webkitNotifications.requestPermission(callback);
    }
    function notification (){
        if (window.webkitNotifications.checkPermission() > 0) {
            RequestPermission(notification);
        }
        var title = "title", icon = "icon.png", body = "body";
        var popup = window.webkitNotifications
                    .createNotification(icon, title, body);
        popup.show();
        setTimeout(function(){ popup.cancel(); }, '15000');
    }
@@@

<script>
    function RequestPermission (callback){
        window.webkitNotifications.requestPermission(callback);
    }
    function notification (){
        if (window.webkitNotifications.checkPermission() > 0) {
            RequestPermission(notification);
        }
        var title = "Guangzhou Tech Party",
            icon = "http://tp4.sinaimg.cn/1644902943/50/5607676780/1",
            body = "Hi, all!";
        var popup = window.webkitNotifications
                    .createNotification(icon, title, body);
        popup.show();
        setTimeout(function(){ popup.cancel(); }, '15000');
    }
</script>

!SLIDE

# Canvas [长微博]

@@@ js
    var can = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    ctx.font = "30pt Ubuntu";
    ctx.fillStyle = "white";
	ctx.fillRect(0, 0, can.width, can.height);
    ctx.fillStyle = "black";
    ctx.fillText("FaWave", 20, 30);
@@@

!SLIDE

# 大公司的简单Canvas应用？

<br/>

> ### [Apple Mobile Me 登录页](http://me.com/)
>
> ### [Google Android 主页](http://www.android.com/)

<br/>
<a href="https://developer.mozilla.org/cn/Canvas_tutorial" style="color:#999">Canvas教程</a>

!SLIDE

# Web Socket 
### &
# Web Worker

!SLIDE

# THANKS
<br/>
#### by [@QLeelulu](http://t.sina.com.cn/qleelulu)

!SLIDE



