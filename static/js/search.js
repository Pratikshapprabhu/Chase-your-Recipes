function save_recipe(recipe_id) {
        console.log(recipe_id)
        $.ajax({
                type:'POST',
                url:'{% url "cookbook:save_recipe" %}',
            data:
            {
                index:recipe_id,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                  alert('Saved');
                    }
        })
}
 // document.on('#recipe_sub',function(e){
 //        e.preventDefault();
 //         console.log("clicked" + $("#recipe_sub").val())
 //        $.ajax({
 //            type:'POST',
 //                url:'{% url "cookbook:save_recipe" %}',
 //            data:
 //            {
 //                id:$("#recipe_sub").val(),
 //            },
 //            success:function(){
 //                  alert('Saved');
 //                    }
 //            })
 //        });
