const spinner = document.getElementById('spinner')
const tableBody = document.getElementById('table-body-box')

$.ajax({
    type: 'GET',
    url: '/ohome/dtClasses/',
    success: function (response) {
        setTimeout(() => {
            spinner.classList.add('not-visible')
            for (const item of response) {
                tableBody.innerHTML += `
                <tr>
                <td class="px-2 py-1 align-middle text-center">
                <a class="link-dark noundline" href="${item.id}">
                ${item.Classe_name} ${item.school_year}
                </a>
                </td>
                <td class="px-2 py-1 align-middle text-center">
                <div class="col">
            <a class="btn btn-outline-info btn-sm link-dark noundline" href="${item.Classe_name}/o_attendence/"
                title="See Attendace of ${item.Classe_name}"><i class="fa fa-eye"></i>
            </a>
            <a class="btn btn-outline-primary btn-sm link-dark noundline" href="${item.Classe_name}/${item.school_year}/${item.id}/o_attmgt/"
                title="Add Attendace to ${item.Classe_name}"><i class="fa fa-edit"></i>
            </a>
        </div>
                </td>
                </tr>
                `
            }
        }, 500)
    },
    error: function (error) {
        setTimeout(() => {
            spinner.classList.add('not-visible')
            tableBody.innerHTML += `
                <p>Failed to load data</p>
                `
        }, 500)
    }
})