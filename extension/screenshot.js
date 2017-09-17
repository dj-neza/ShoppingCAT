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
	    /*console.log(e.detail.x);
	    console.log(e.detail.y);
	    console.log(e.detail.width);
	    console.log(e.detail.height);
	    console.log(e.detail.rotate);
	    console.log(e.detail.scaleX);
	    console.log(e.detail.scaleY);*/
	  }
	});
}

document.getElementById('buttons').onclick = function (event) {
	var e = event || window.event;
    	var target = e.target || e.srcElement;
   	var result, result2;
	var input;
	var data;
	result = cropper["getCroppedCanvas"]('{ "maxWidth": 4096, "maxHeight": 4096 }');
	console.log(result);
	var canvasData = result.toDataURL();


	var img = new Image();
	img.src = result;
	var formData = new FormData();
	//console.log(result);
	//console.log(canvasData);
	//console.log(img.src);
	formData.append('user', 1);
	formData.append('image', result.toDataURL("image/png"));

	//console.log(JSON.stringify({"user": 1, "image": result.toDataURL("image/png")}));

	//console.log(img);

	result2 = result.toBlob(function (blob) {
		var formData = new FormData();
		formData.append('image', blob);
		formData.append('user', 1);
		$.ajax("http://localhost:8000/capi/inspiration/", {
		  method: "POST",
		  data: formData,
		  processData: false,
		  contentType: false,
		  success: function() {console.log('SUCCESS!');},
		  error: function() {console.log('Upload error');}
		});
	});

	

	/*$.post("http://localhost:8000/capi/inspiration/",
    {
        user: 1,
        image: ""
    },
    function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });*/

	document.getElementById("cropped").innerHTML += '<img src="' + canvasData + '">';
};

