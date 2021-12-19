$(document).ready(function() {
	var ingredientwrapper   		= $(".input_ingredients_wrap");
	var add_button      = $(".add_ingredient_button");
	
	var y = 1;
	$(add_button).click(function(e){
		e.preventDefault();
			y++;
			$(ingredientwrapper).append('<div><input class = "submitInputSmaller" type="text" name="ingredient"><a href="#" class="remove_field" required><i class="fas fa-minus"></i></a></div>');
	});
	
	$(ingredientwrapper).on("click",".remove_field", function(e){
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});

$(document).ready(function() {
	var stepwrapper   		= $(".input_steps_wrap");
	var add_button      = $(".add_step_button");
	
	var x = 1;
	$(add_button).click(function(e){
		e.preventDefault();
			x++;
			$(stepwrapper ).append('<div><input class = "submitInputSmaller" type="text" name="step"><a href="#" class="remove_field" required><i class="fas fa-minus"></i></a></div>');
	});
	
	$(stepwrapper ).on("click",".remove_field", function(e){
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});