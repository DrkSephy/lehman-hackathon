$(".btn-group-vertical")
.children()
.on("click", function() {
	var className = $(this).html();
	console.log(className);
	$("#cancelTitle").html("Notify " + className);
});

$("#addBtn")
.on("click", function() {

	// ajax here
});
