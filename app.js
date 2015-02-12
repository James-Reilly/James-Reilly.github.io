/**
 * Created by jreilly on 2/10/15.
 */
var app = document.querySelector('#app');
app.page = 'about';

app.menuItemSelected = function(e, detail, sender) {
    if (detail.isSelected) {
        document.querySelector('#scaffold').closeDrawer();
    }
};