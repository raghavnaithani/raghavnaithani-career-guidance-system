document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      console.log('Backend response:', result); // For debugging
      // Redirect to results page (or update DOM)
      window.location.href = '/result'; 
    } catch (error) {
      console.error('Error:', error);
    }
  });
});