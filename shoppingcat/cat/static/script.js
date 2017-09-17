var style_me_objects = [];

function api(imgurl) {
	//var imgurl = $('#picture').val();
	//console.log(imgurl);
	style_me_objects = [];
	$("#pop2_objects").empty();
	var client = new HttpClient();
    client.post(imgurl, function(response) {
        var object = JSON.parse(response);
        //console.log(object);
        returnProduct(object);
        console.log(style_me_objects);

        for (var o = 0; o < style_me_objects.length; o++) {
        	$("#pop2_objects").append("\
        		<div style='display: inline-block; background-color: white; margin: 5px; padding: 5px; margin-top: 6%; min-width: 30%;'> \
                    <div style='text-decoration-color: #34AE95; white-space: initial;'>" + style_me_objects[o].productName + "</div> \
                    <div><img src='" + style_me_objects[o].image + "'/></div> \
                    <button style='margin: 5px; border-radius: 4px; background-color: #34AE95; border:0px solid #34AE95;' >BUY</button> \
                    <button style='margin: 5px; border-radius: 4px; background-color: #34AE95; border:0px solid #34AE95;' >WISHLIST</button> \
                </div>");
        }
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

			style_me_objects.push({
				productName: productName,
				brand: brand,
				price: price,
				shop: shop,
				sku: sku,
				image: image,
				product: product
			});
		}
	}
	/*document.getElementById("productName").innerHTML += productName;
	document.getElementById("category").innerHTML += category;
	document.getElementById("sku").innerHTML += sku;
	document.getElementById("price").innerHTML += price;
	document.getElementById("brand").innerHTML += brand;
	document.getElementById("shop").innerHTML += shop;
	document.getElementById("url").innerHTML += product;
	document.getElementById("productimg").src += image;
	*/
}

function style_me_button(imgurl) {
	api(imgurl);
}

/*
return similars: 
	len = Object.keys(object.similar_products).length;
	object.similar_products[1-len] -- 0 je vecinoma sam produkt
	posamezni podatki naprej isto .sku/.title itd

*/




