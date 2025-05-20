from .ansible import renderTemplate

result = renderTemplate("x: 'test var'", "{{x}}")