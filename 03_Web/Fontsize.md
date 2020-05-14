### Font-size

[Material Design](https://material.io/design/typography/understanding-typography.html#type-properties)

- Work with proportions instead of explicit sizes.
- Rely on default browser font sizes instead of setting it on the `:root`, `<html>` or `<body>`.
- Use `rem` units to help scale content with a user’s personal preferences.
- Avoid making assumptions and let the environment decide how your content is being consumed.

```css
# small: 14px 
# default: 16px
# large: 24px

:root {
  font-size: 62.5%; /* (62.5/100) * 16px = 10px */
  --font-size--small: 1.4rem; /* 14px */
  --font-size--default: 1.6rem; /* 16px */
  --font-size--large: 2.4rem; /* 24px */
}
 
.font-size--small {
  font-size: var(--font-size--small);
}

.font-size--default {
  font-size: var(--font-size--default);
}

.font-size--large {
  font-size: var(--font-size--large);
}
```

- 참고: 브라우저 기본 폰트 크기(Base font size)