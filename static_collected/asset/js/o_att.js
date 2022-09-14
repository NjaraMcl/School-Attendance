const spinner = document.getElementById('spinner')
const tabletitle = document.getElementById('catp')
const tableBody = document.getElementById('table-body-box')

$.ajax({
    type: 'GET',
    url: '/shome/listClasses/',
    success: function (response) {
        tabletitle.innerHTML += `{{ klasname }} ({{ skooY }})`
        tableBody.innerHTML += `
            {% for att in listPresence %}
            {% if att.student.class_id.Classe_name == klasname %}
            <tr>
                <td class="text-center">{{ att.student.class_id.Classe_name }}</td>
                <td class="text-center">{{ att.student }}</td>
                <td class="text-center">{{ att.attendance_date }}</td>
                {% if att.status %}
                <td class="text-center">
                    <p style="color:greenyellow">Présent(e)</p>
                </td>
                {% else %}
                <td class="text-center">
                    <p style="color:red">Abscent(e)
                </td>
                {% endif %}
            </tr>
            {% endif %}
            {% endfor %}
              `
        spinner.classList.add('not-visible')
    },
    error: function (error) {
        console.log(error)
    }
})