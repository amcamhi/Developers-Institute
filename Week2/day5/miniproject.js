function my_function(num) {
  form.display.value += num
}

function equal() {
  let exp = form.display.value
  if (exp) {
      form.display.value = eval(exp)
  }
}

function allClear() {
  let exp = form.display.value
  form.display.value = exp.substring(0, exp.lenght -1)
}