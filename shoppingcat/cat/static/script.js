function api() {
	var imgurl = $('#picture').val();
	console.log(imgurl);
	var client = new HttpClient();
	    client.post(imgurl, function(response) {
	        var object = JSON.parse(response);
	        console.log(object);
	        returnProduct(object);
	    });
	
}
function simil() {
	var sku = "PC721D05G-Q11";
	var url = "http://www.fashwell.com/api/hackzurich/v1/similarity/";
	url += sku;
	url += "/";
	var client = new HttpClient();
    	client.get(url, function(response) {
        	var object = JSON.parse(response);
        	console.log(object);
        });
}

var HttpClient = function() {
	this.post = function(imgurl, callBack) {
		var params = {
			/*
			"shop_name":"siroop"/"zalando",
			"min_price":integer,
			"max_price":integer,
			"max_products_per_detection":integer,
			*/
		  "url":imgurl
		}
		var url = "http://www.fashwell.com/api/hackzurich/v1/posts/";
		var access_token = "d7881ccfab3d97615a8989ff1e9f00c170f94e8a";
	        var xhr = new XMLHttpRequest();
	        xhr.onreadystatechange = function() {
	        	if (xhr.readyState == 4 && xhr.status == 200)
	                	callBack(xhr.responseText);
	        }
	        xhr.open("POST", url);
	        xhr.setRequestHeader('Authorization', 'Token ' + access_token);
	        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	        //xhr.onload = requestComplete;
	        xhr.send(JSON.stringify(params));
	}
	this.get = function(url, callBack) {
		var access_token = "d7881ccfab3d97615a8989ff1e9f00c170f94e8a";
	        var xhr = new XMLHttpRequest();
	        xhr.onreadystatechange = function() {
	            if (xhr.readyState == 4 && xhr.status == 200)
	                callBack(xhr.responseText);
	        }
	        xhr.open( "GET", url, true );
	        xhr.setRequestHeader('Authorization', 'Token ' + access_token);
	        xhr.send( null );
	}
}

function returnProduct(object) {
	//get number of categories
	var length = Object.keys(object.products).length;
	var category, productNum, productName, brand, price, shop, sku, image, product;
	//loop through categories
	for (i=0; i<length; i++) {
		//get category name
		category = object.products[i].category;
		//get number of products in category
		productNum = Object.keys(object.products[i].instances).length;
		for (j=0; j < productNum; j++) {
			productName = object.products[i].instances[j].title;
			brand = object.products[i].instances[j].brand_name;
			price = object.products[i].instances[j].price;
			shop = object.products[i].instances[j].shop_name;
			sku = object.products[i].instances[j].sku;
			image = object.products[i].instances[j].img_url;
			product = object.products[i].instances[j].product_url;
		}
	}
	document.getElementById("productName").innerHTML += productName;
	document.getElementById("category").innerHTML += category;
	document.getElementById("sku").innerHTML += sku;
	document.getElementById("price").innerHTML += price;
	document.getElementById("brand").innerHTML += brand;
	document.getElementById("shop").innerHTML += shop;
	document.getElementById("url").innerHTML += product;
	document.getElementById("productimg").src += image;
}

/*
return similars: 
	len = Object.keys(object.similar_products).length;
	object.similar_products[1-len] -- 0 je vecinoma sam produkt
	posamezni podatki naprej isto .sku/.title itd

*/




