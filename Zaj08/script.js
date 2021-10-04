function printFormData() {
    console.log(document.forms[0].elements[0].value)
    // zwroty:
    // - string dla liczby
    // - string dla tekstu
    // - pusty string dla braku wartości

    console.log(document.forms[0].elements[1].value)
    // zwroty:
    // - string dla liczby
    // - string dla tekstu
    // - pusty string dla braku wartości
}
document.forms[0].elements[2].onclick = printFormData