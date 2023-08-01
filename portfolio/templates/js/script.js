// portfolio/static/portfolio/js/script.js

// Função para exibir e ocultar a descrição do projeto
function toggleDescription(projectId) {
    const projectDescription = document.getElementById(`project-description-${projectId}`);
    projectDescription.classList.toggle('show-description');
}

// Event listener para os botões "Exibir Descrição"
const toggleButtons = document.querySelectorAll('.toggle-button');
toggleButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const projectId = button.dataset.projectId;
        toggleDescription(projectId);
    });
});
