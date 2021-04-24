document.addEventListener('DOMContentLoaded', (event) => {

    let regexMap = {
        name: new RegExp("^.{4,}$"),
        surname: new RegExp("^.{4,}$"),
        city: new RegExp("^.{4,}$"),
        'vk/email': new RegExp("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\\])"),
        place: new RegExp("^.{4,}$"),
        date: new RegExp("^(\\d{4}\-)(\\d{2}\-)(\\d{2})$"),
    }

    function setInvalidRegx(line, error_div) {
        line.setAttribute('style', 'background: red;');
        line.classList.add('line-error');
        error_div.setAttribute('style', 'display: block');
    }

    function setValidRegx(line, error_div) {
        line.setAttribute('style', 'background: #1abc9c;');
        line.classList.remove('line-error');
        error_div.setAttribute('style', 'display: none');
    }

    function focusInEmptyInput() {
        let line = this.nextElementSibling;
        let error_div = line.nextElementSibling;
        let regex = regexMap[this.id]
        if (!regex.test(this.value)) {
            setInvalidRegx(line, error_div)
        } else {
            setValidRegx(line, error_div)
        }
    }

    function focusOutEmptyInput() {
        let line = this.nextElementSibling;
        let error_div = line.nextElementSibling;
        let regex = regexMap[this.id]
        if (!regex.test(this.value)) {
            setInvalidRegx(line, error_div)
        } else {
            setValidRegx(line, error_div)
        }
    }


    let form_elements = document.getElementsByClassName('form-input');
    for (let input_el of form_elements) {
        input_el.addEventListener('focusin', focusInEmptyInput, false)
        input_el.addEventListener('focusout', focusOutEmptyInput, false)
    }
});
