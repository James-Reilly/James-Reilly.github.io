/**
 * Created by jreilly on 2/10/15.
 */

Polymer({});
var app = document.querySelector('#app');
app.page = 'about';
console.log("Scripts! amirite? ");

var tabs = document.querySelector('#tabs');
var list = document.querySelector('post-list');
  tabs.addEventListener('core-select', function() {
  	console.log("Selected: " + tabs.selected);
    list.show = tabs.selected;
 });

app.menuItemSelected = function(e, detail, sender) {
    if (detail.isSelected) {
        document.querySelector('#scaffold').closeDrawer();
    }
};