console.log('working');
if(localStorage.getItem('save') == null){
var save = {};
}
else
{
  save = JSON.parse(localStorage.getItem('save'));
document.getElementById('save').innerHTML = Object.keys(save).length;
}
$('.save').click(function(){
console.log('clicked');
var idstr = this.id.toString();
console.log(idstr);
if (save[idstr] !=undefined){
  save[idstr] = save[idstr] + 1;
}
else
{
  save[idstr] = 1;
}
console.log(save);
localStorage.setItem('save', JSON.stringify(save));
document.getElementById('save').innerHTML = Object.keys(save).length;
});
$('#popcart').popover();
document.getElementById("popcart").setAttribute('data-content', '<h5>Cart for your items in my shopping cart</h5>');
