$(document).ready(function() {
	var max_fields      = 10;
	var wrapper   		= $(".input_fields_wrap");
	var add_button      = $(".add_field_button");
	
	var x = 1;
	$(add_button).click(function(e){
		e.preventDefault();
			x++;
			$(wrapper).append('<div><input type="text" name="stepTest"/><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
	});
	
	$(wrapper).on("click",".remove_field", function(e){
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});