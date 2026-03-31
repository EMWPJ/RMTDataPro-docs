// Remove ignore classes and trigger MathJax typeset
window.addEventListener('load', function() {
    // Remove the ignore classes from article body
    var articleBody = document.querySelector('[itemprop="articleBody"]');
    if (articleBody) {
        articleBody.classList.remove('tex2jax_ignore', 'mathjax_ignore');
    }
    
    // Also remove from any .math elements
    document.querySelectorAll('.math').forEach(function(el) {
        el.classList.remove('tex2jax_ignore', 'mathjax_ignore');
    });
    
    // Trigger MathJax typeset
    if (window.MathJax) {
        MathJax.typesetPromise().catch(function(err) {
            console.log('MathJax typeset error:', err);
        });
    }
});
