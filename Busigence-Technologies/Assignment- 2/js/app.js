// MYSQL Checkbox
function showmysqlcontent() {
    var checkbox = document.getElementById('mysqlcheckbox');
    var change = document.getElementById('mysqlcontent');
    var change2 = document.getElementById('sourcemysql');
    
    var change3 = document.getElementById('mysqlvisual');

    if (checkbox.checked == true) {
        change.style.display="block";
        change2.style.display="block";
       
        change3.style.display="block";
    } else {
        change.style.display="none";
        change2.style.display="none";
        change3.style.display="none";
    }
}
// CSV Checkbox
function showcsvcontent() {
    var checkbox = document.getElementById('csvcheckbox');
    var change = document.getElementById('csvcontent');
    var change2 = document.getElementById('sourcecsv');
    var change3 = document.getElementById('csvvisual');
    if (checkbox.checked == true) {
        change.style.display="block";
        change2.style.display="block";
        change3.style.display="block";
    } else {
        change.style.display="none";
        change2.style.display="none";
        change3.style.display="none";
    }
}
// Select Source MYSQL
function showmysql() {
    var checkbox = document.getElementById('mysqlsource');
    var change2 = document.getElementById('sourcemysql');
    if (checkbox.checked == true) {
        change2.style.display="block";
    } else {
        change2.style.display="none";
    }
}
// Select Source CSV
function showcsv() {
    var checkbox = document.getElementById('csvsource');
    var change2 = document.getElementById('sourcecsv');
    if (checkbox.checked == true) {
        change2.style.display="block";
    } else {
        change2.style.display="none";
    }
}