/**
 * Helper JS for rt.zptformfield autocomplete lines field
 */

(function($) {

	$(document).ready(function() {
		
		$('.zptformfield .newAutocompleteLinesField').each(function() {
			var $this = $(this);
			var container = $this.closest('.zptformfield');
			var source = container.data('ajax-source');
			$this.autocomplete({
				source: source,
		        minLength: 2,
		        select: function(event, ui) {
					if ($('.fieldValues input[value="'+ui.item.value+'"]', container).length>0) {
		            	$this.val('');
						return false;
					}
					var newFieldRow = $('.fieldModel li', container).clone(true);
					var newField = newFieldRow.find('input');
					var fieldName = container.data('fieldname');
					newFieldRow.find('strong').text(ui.item.label);
					newField.prop('name', fieldName+':list');
					newField.val(ui.item.value);
					$('.fieldValues', container).append(newFieldRow);
		            $this.val('');
					return false;
		        }
			});			
		});
						
		$('.zptformfield .deleteItem').click(function(event){
			event.preventDefault();
			$(this).closest('li').remove();
		});
		
	});

})(jQuery);