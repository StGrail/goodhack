document.addEventListener('DOMContentLoaded', (event) => {

    let regexMap = {
        name: new RegExp("^.{3,}$"),
        surname: new RegExp("^.{3,}$"),
        city: new RegExp("^.{3,}$"),
        'vk/email': new RegExp("^.{3,}$"),
        place: new RegExp("^.{3,}$"),
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

    function removeFocusOutError(line, error_div) {
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
            removeFocusOutError(line, error_div)
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
