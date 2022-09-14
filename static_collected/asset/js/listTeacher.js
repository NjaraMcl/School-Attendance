const spinner = document.getElementById('spinner')
const tableBody = document.getElementById('table-body-box')

$.ajax({
    type: 'GET',
    url: '/ohome/dtTeacher/',
    success: function (response) {
        setTimeout(() => {
            spinner.classList.add('not-visible')
            for (const item of response) {
                tableBody.innerHTML += `
                <tr>
                <td class="px-2 py-1 align-middle text-center">
                ${item.nom} ${item.prenom}
                </td>
                <td class="px-2 py-1 align-middle text-center">
                ${item.gender}
                </td>
                </tr>
                `
            }
        }, 500)
    },
    error: function (error) {
        console.log(error)
        setTimeout(() => {
            spinner.classList.add('not-visible')
            tableBody.innerHTML += `
                <p>Failed to load data</p>
                `
        }, 500)
    }
})