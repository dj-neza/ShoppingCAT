/**
 *  @author ShoppingCAT
 *  2017
 */

var cropper;
function setScreenshotUrl(url) {
  document.getElementById('target').src = url;
        var image = document.getElementById('target');
	cropper = new Cropper(image, {
	  aspectRatio: NaN,
	  minCropBoxWidth: 200,
	  minCropBoxHeight: 200,
	  crop: function(e) {
	    console.log(e.detail.x);
	    console.log(e.detail.y);
	    console.log(e.detail.width);
	    console.log(e.detail.height);
	    console.log(e.detail.rotate);
	    console.log(e.detail.scaleX);
	    console.log(e.detail.scaleY);
	  }
	});
}

document.getElementById('buttons').onclick = function (event) {
	var e = event || window.event;
    	var target = e.target || e.srcElement;
   	var result;
    	var input;
    	var data;
    	result = cropper["getCroppedCanvas"]('{ "maxWidth": 4096, "maxHeight": 4096 }');
    	console.log(result);
    	var canvasData = result.toDataURL();
	document.getElementById("cropped").innerHTML += '<img src="' + canvasData + '">';
};

