< !doctyhtml >
< head >
< link
href = "css/newstyle.css"
rel = "stylesheet"
type = "text/css" >
< script >
function
validateForm()
{
    var
firstname = document.getElementById("Fname").value;
var
lastname = document.getElementById("lname").value;
var
sname = document.getElementById("sname").value;
var
selmonth = document.getElementById("selmonth").value;
var
selday = document.getElementById("selday").value;
var
selyear = document.getElementById("selyear").value;
var
gen = document.getElementById("rad").checked;
var
con = document.getElementById("country").value;
var
email = document.getElementById("email").value;
var
phone = document.getElementById("phone").value;
var
pass=document.getElementById("pass").value;
var
confirm = document.getElementById("confirm").value;
var
check = document.getElementById("check").checked;

if (firstname == "" | | firstname == null)
{
    window.alert("please fill first name");
return false;
}
if (lastname == "" | | lastname == null){
window.alert("please fill last name");
return false;
}
if (sname == "" | | sname == null){
window.alert("please fill screen name");
return false;
}
if (selmonth == 0)
{
window.alert("please select a month");
// selmonth.focus();
return false;
}
if (selday == 0)
{
window.alert("please select a day");
// selday.focus();
return false;
}
if (selyear == 0)
{
window.alert("please select a year");
// selyear.focus();
return false;
}
if (gen == false){
window.alert("please select gender");
return false;
}
if (con == 0){
window.alert("please select a country");
return false;
}
if (email == "" | | email == null){
window.alert("please enter your email");
return false;
}
if (phone == "" | | phone == null){
window.alert("please enter your contact number");
return false;
}
if (pass == "" | | pass == null){
window.alert("please enter your password");
return false;
}
if (confirm == "" | | confirm == null){
window.alert("please enter your confirm password");
return false;
}
if (check == false){
window.alert("please enter checkbox to proceed");
return false;
}
return true;
}
< / script >
    < / head >
        < body >
        < form
action = "vowel.html"
method = "GET"
target = "_blank"
autocomplete = "off"
name = "form1"
enctype = "multipart/form-data"
onsubmit = "return validateForm()" >

           < table


class ="sample" >

< tr >
< th
colspan = "2" > Sign
up < / th >
< / tr >
< tr >
< td


class ="one" > First Name < span class ="sup" > * < / span > < / td >

< td


class ="text1" > < input type="text" class ="fname" id="fname" name="fname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required >
< / td >
< / tr >
< tr >
< td


class ="one" > Last Name < / td >

< td


class ="text1" > < input type="text" class ="" id="lname" name="fname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Screen Name < / td >

< td


class ="text1" > < input type="text" class ="" id="sname" name="sname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Date of Birth < / td >

< td > < select
name = "months"
id = "selmonth"


class ="cl1" required >

< option
value = "" > sel < / option >
< option
value = "jan" > January < / option >
< option
value = "feb" > feb < / option >
< option
value = "mar" > Mar < / option >
< / select >
< select
required
name = "days"
id = "selday"


class ="cl2" required >

< option
value = "" > sel < / option >
< option
value = "one" > 1 < / option >
< option
value = "two" > 2 < / option >
< option
value = "three" > 3 < / option >
< / select >
< select
required
name = "days"
id = "selyear"


class ="cl3" required >

< option
value = "" > sel < / option >
< option
value = "asd" > 1990 < / option >
< option
value = "qwe" > 2000 < / option >
< option
value = "ddf" > 2001 < / option >
< / select >
< / td >
< / tr >
< tr >
< td


class ="one" > Gender < / td >

< td > < input
type = "radio"


class ="" id="rad" name="gender" value="m" required > male

< input
type = "radio"


class ="" id="" name="gender" value="f" required > female

< / td >
< / tr >
< tr >

< tr >
< td


class ="one" > Country < / td >

< td > < select
name = "country"
id = "country"


class ="cl4" required >

< option
value = "" > Select
a
Country < / option >
< option
value = "india" > India < / option >
< option
value = "pakistan" > Pakistan < / option >
< option
value = "china" > China < / option >
< / select > < / td >
< / tr >
< tr >
< td


class ="one" > Email < span class ="sup" > * < / span > < / td >

< td > < input
type = "email"


class ="" id="email" name="email"


pattern = "^[\w]{1,}[\w.+-]{0,}@[\w-]{2,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$"
placeholder = "enter your email"
onclick = "validEmail()" > < / td >
< / tr >
< / tr >
< td


class ="one" > Phone number < / td >

< td > < input
type = "tel"


class ="" id="phone" name="number"


placeholder = "format(xxxx-xxx-xxx)"
pattern = "^\d{4}-\d{3}-\d{3}$"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Password < span class ="sup" > * < / span > < / td >

< td > < input
type = "password"


class ="pass" id="pass"


pattern = "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
placeholder = "enter your password"
title = "Must contain at least one number and one uppercase and lowercase letter,
and at
least
8 or more
characters
" required></td>
< / tr >
< tr >
< td


class ="one" > Confirm Password < span class ="sup" > * < / span > < / td >

< td > < input
type = "password"


class ="confirm" id="confirm"


placeholder = "enter your password"
required > < / td >
< / tr >
< tr >
< td > < / td >
< td > < input
type = "checkbox"


class ="" id="check" name="name" value="s" required >


I
agree
to
the
Terms
of
use < / td >

< / tr >

< tr >
< td
colspan = "2"


class ="col" >

< input
type = "button"
value = "cancel"
name = "cancel"
style = "float:right" >
< input
type = "submit"
value = "submit"
name = "submit"
style = "float:right" >

< / td >
< / tr >
< / table >
< / form >
< / body >
< !doctype
html >
< head >
< link
href = "css/newstyle.css"
rel = "stylesheet"
type = "text/css" >
< script >
function
validateForm()
{
    var
firstname = document.getElementById("Fname").value;
var
lastname = document.getElementById("lname").value;
var
sname = document.getElementById("sname").value;
var
selmonth = document.getElementById("selmonth").value;
var
selday = document.getElementById("selday").value;
var
selyear = document.getElementById("selyear").value;
var
gen = document.getElementById("rad").checked;
var
con = document.getElementById("country").value;
var
email = document.getElementById("email").value;
var
phone = document.getElementById("phone").value;
var
pass=document.getElementById("pass").value;
var
confirm = document.getElementById("confirm").value;
var
check = document.getElementById("check").checked;

if (firstname == "" | | firstname == null)
{
    window.alert("please fill first name");
return false;
}
if (lastname == "" | | lastname == null){
window.alert("please fill last name");
return false;
}
if (sname == "" | | sname == null){
window.alert("please fill screen name");
return false;
}
if (selmonth == 0)
{
window.alert("please select a month");
// selmonth.focus();
return false;
}
if (selday == 0)
{
window.alert("please select a day");
// selday.focus();
return false;
}
if (selyear == 0)
{
window.alert("please select a year");
// selyear.focus();
return false;
}
if (gen == false){
window.alert("please select gender");
return false;
}
if (con == 0){
window.alert("please select a country");
return false;
}
if (email == "" | | email == null){
window.alert("please enter your email");
return false;
}
if (phone == "" | | phone == null){
window.alert("please enter your contact number");
return false;
}
if (pass == "" | | pass == null){
window.alert("please enter your password");
return false;
}
if (confirm == "" | | confirm == null){
window.alert("please enter your confirm password");
return false;
}
if (check == false){
window.alert("please enter checkbox to proceed");
return false;
}
return true;
}
< / script >
    < / head >
        < body >
        < form
action = "vowel.html"
method = "GET"
target = "_blank"
autocomplete = "off"
name = "form1"
enctype = "multipart/form-data"
onsubmit = "return validateForm()" >

           < table


class ="sample" >

< tr >
< th
colspan = "2" > Sign
up < / th >
< / tr >
< tr >
< td


class ="one" > First Name < span class ="sup" > * < / span > < / td >

< td


class ="text1" > < input type="text" class ="fname" id="fname" name="fname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required >
< / td >
< / tr >
< tr >
< td


class ="one" > Last Name < / td >

< td


class ="text1" > < input type="text" class ="" id="lname" name="fname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Screen Name < / td >

< td


class ="text1" > < input type="text" class ="" id="sname" name="sname"


pattern = "[a-zA-Z]{3,}"
placeholder = "enter a name"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Date of Birth < / td >

< td > < select
name = "months"
id = "selmonth"


class ="cl1" required >

< option
value = "" > sel < / option >
< option
value = "jan" > January < / option >
< option
value = "feb" > feb < / option >
< option
value = "mar" > Mar < / option >
< / select >
< select
required
name = "days"
id = "selday"


class ="cl2" required >

< option
value = "" > sel < / option >
< option
value = "one" > 1 < / option >
< option
value = "two" > 2 < / option >
< option
value = "three" > 3 < / option >
< / select >
< select
required
name = "days"
id = "selyear"


class ="cl3" required >

< option
value = "" > sel < / option >
< option
value = "asd" > 1990 < / option >
< option
value = "qwe" > 2000 < / option >
< option
value = "ddf" > 2001 < / option >
< / select >
< / td >
< / tr >
< tr >
< td


class ="one" > Gender < / td >

< td > < input
type = "radio"


class ="" id="rad" name="gender" value="m" required > male

< input
type = "radio"


class ="" id="" name="gender" value="f" required > female

< / td >
< / tr >
< tr >

< tr >
< td


class ="one" > Country < / td >

< td > < select
name = "country"
id = "country"


class ="cl4" required >

< option
value = "" > Select
a
Country < / option >
< option
value = "india" > India < / option >
< option
value = "pakistan" > Pakistan < / option >
< option
value = "china" > China < / option >
< / select > < / td >
< / tr >
< tr >
< td


class ="one" > Email < span class ="sup" > * < / span > < / td >

< td > < input
type = "email"


class ="" id="email" name="email"


pattern = "^[\w]{1,}[\w.+-]{0,}@[\w-]{2,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$"
placeholder = "enter your email"
onclick = "validEmail()" > < / td >
< / tr >
< / tr >
< td


class ="one" > Phone number < / td >

< td > < input
type = "tel"


class ="" id="phone" name="number"


placeholder = "format(xxxx-xxx-xxx)"
pattern = "^\d{4}-\d{3}-\d{3}$"
required > < / td >
< / tr >
< tr >
< td


class ="one" > Password < span class ="sup" > * < / span > < / td >

< td > < input
type = "password"


class ="pass" id="pass"


pattern = "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
placeholder = "enter your password"
title = "Must contain at least one number and one uppercase and lowercase letter,
and at
least
8 or more
characters
" required></td>
< / tr >
< tr >
< td


class ="one" > Confirm Password < span class ="sup" > * < / span > < / td >

< td > < input
type = "password"


class ="confirm" id="confirm"


placeholder = "enter your password"
required > < / td >
< / tr >
< tr >
< td > < / td >
< td > < input
type = "checkbox"


class ="" id="check" name="name" value="s" required >


I
agree
to
the
Terms
of
use < / td >

< / tr >

< tr >
< td
colspan = "2"


class ="col" >

< input
type = "button"
value = "cancel"
name = "cancel"
style = "float:right" >
< input
type = "submit"
value = "submit"
name = "submit"
style = "float:right" >

< / td >
< / tr >
< / table >
< / form >
< / body >

