# Design Tokens Reference

Complete design token system for building consistent, scalable design systems.

---

## Token Architecture

### Three-Tier Token System

```
┌─────────────────────────────────────────────────────────────┐
│                    GLOBAL TOKENS                            │
│           (Primitives - Raw values)                         │
│                                                             │
│   --color-blue-500: #3B82F6                                │
│   --space-4: 16px                                          │
│   --font-size-base: 16px                                   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    ALIAS TOKENS                             │
│           (Semantic - Purpose-driven)                       │
│                                                             │
│   --color-primary: var(--color-blue-500)                   │
│   --spacing-md: var(--space-4)                             │
│   --text-body: var(--font-size-base)                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  COMPONENT TOKENS                           │
│           (Specific - Component-scoped)                     │
│                                                             │
│   --button-bg: var(--color-primary)                        │
│   --button-padding: var(--spacing-md)                      │
│   --button-font-size: var(--text-body)                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Color Tokens

### Global Color Palette

```css
:root {
  /* Gray Scale */
  --color-gray-50: #F9FAFB;
  --color-gray-100: #F3F4F6;
  --color-gray-200: #E5E7EB;
  --color-gray-300: #D1D5DB;
  --color-gray-400: #9CA3AF;
  --color-gray-500: #6B7280;
  --color-gray-600: #4B5563;
  --color-gray-700: #374151;
  --color-gray-800: #1F2937;
  --color-gray-900: #111827;
  --color-gray-950: #030712;

  /* Blue (Primary) */
  --color-blue-50: #EFF6FF;
  --color-blue-100: #DBEAFE;
  --color-blue-200: #BFDBFE;
  --color-blue-300: #93C5FD;
  --color-blue-400: #60A5FA;
  --color-blue-500: #3B82F6;
  --color-blue-600: #2563EB;
  --color-blue-700: #1D4ED8;
  --color-blue-800: #1E40AF;
  --color-blue-900: #1E3A8A;
  --color-blue-950: #172554;

  /* Indigo */
  --color-indigo-50: #EEF2FF;
  --color-indigo-100: #E0E7FF;
  --color-indigo-200: #C7D2FE;
  --color-indigo-300: #A5B4FC;
  --color-indigo-400: #818CF8;
  --color-indigo-500: #6366F1;
  --color-indigo-600: #4F46E5;
  --color-indigo-700: #4338CA;
  --color-indigo-800: #3730A3;
  --color-indigo-900: #312E81;
  --color-indigo-950: #1E1B4B;

  /* Purple */
  --color-purple-50: #FAF5FF;
  --color-purple-100: #F3E8FF;
  --color-purple-200: #E9D5FF;
  --color-purple-300: #D8B4FE;
  --color-purple-400: #C084FC;
  --color-purple-500: #A855F7;
  --color-purple-600: #9333EA;
  --color-purple-700: #7E22CE;
  --color-purple-800: #6B21A8;
  --color-purple-900: #581C87;
  --color-purple-950: #3B0764;

  /* Pink */
  --color-pink-50: #FDF2F8;
  --color-pink-100: #FCE7F3;
  --color-pink-200: #FBCFE8;
  --color-pink-300: #F9A8D4;
  --color-pink-400: #F472B6;
  --color-pink-500: #EC4899;
  --color-pink-600: #DB2777;
  --color-pink-700: #BE185D;
  --color-pink-800: #9D174D;
  --color-pink-900: #831843;
  --color-pink-950: #500724;

  /* Red */
  --color-red-50: #FEF2F2;
  --color-red-100: #FEE2E2;
  --color-red-200: #FECACA;
  --color-red-300: #FCA5A5;
  --color-red-400: #F87171;
  --color-red-500: #EF4444;
  --color-red-600: #DC2626;
  --color-red-700: #B91C1C;
  --color-red-800: #991B1B;
  --color-red-900: #7F1D1D;
  --color-red-950: #450A0A;

  /* Orange */
  --color-orange-50: #FFF7ED;
  --color-orange-100: #FFEDD5;
  --color-orange-200: #FED7AA;
  --color-orange-300: #FDBA74;
  --color-orange-400: #FB923C;
  --color-orange-500: #F97316;
  --color-orange-600: #EA580C;
  --color-orange-700: #C2410C;
  --color-orange-800: #9A3412;
  --color-orange-900: #7C2D12;
  --color-orange-950: #431407;

  /* Amber */
  --color-amber-50: #FFFBEB;
  --color-amber-100: #FEF3C7;
  --color-amber-200: #FDE68A;
  --color-amber-300: #FCD34D;
  --color-amber-400: #FBBF24;
  --color-amber-500: #F59E0B;
  --color-amber-600: #D97706;
  --color-amber-700: #B45309;
  --color-amber-800: #92400E;
  --color-amber-900: #78350F;
  --color-amber-950: #451A03;

  /* Yellow */
  --color-yellow-50: #FEFCE8;
  --color-yellow-100: #FEF9C3;
  --color-yellow-200: #FEF08A;
  --color-yellow-300: #FDE047;
  --color-yellow-400: #FACC15;
  --color-yellow-500: #EAB308;
  --color-yellow-600: #CA8A04;
  --color-yellow-700: #A16207;
  --color-yellow-800: #854D0E;
  --color-yellow-900: #713F12;
  --color-yellow-950: #422006;

  /* Lime */
  --color-lime-50: #F7FEE7;
  --color-lime-100: #ECFCCB;
  --color-lime-200: #D9F99D;
  --color-lime-300: #BEF264;
  --color-lime-400: #A3E635;
  --color-lime-500: #84CC16;
  --color-lime-600: #65A30D;
  --color-lime-700: #4D7C0F;
  --color-lime-800: #3F6212;
  --color-lime-900: #365314;
  --color-lime-950: #1A2E05;

  /* Green */
  --color-green-50: #F0FDF4;
  --color-green-100: #DCFCE7;
  --color-green-200: #BBF7D0;
  --color-green-300: #86EFAC;
  --color-green-400: #4ADE80;
  --color-green-500: #22C55E;
  --color-green-600: #16A34A;
  --color-green-700: #15803D;
  --color-green-800: #166534;
  --color-green-900: #14532D;
  --color-green-950: #052E16;

  /* Emerald */
  --color-emerald-50: #ECFDF5;
  --color-emerald-100: #D1FAE5;
  --color-emerald-200: #A7F3D0;
  --color-emerald-300: #6EE7B7;
  --color-emerald-400: #34D399;
  --color-emerald-500: #10B981;
  --color-emerald-600: #059669;
  --color-emerald-700: #047857;
  --color-emerald-800: #065F46;
  --color-emerald-900: #064E3B;
  --color-emerald-950: #022C22;

  /* Teal */
  --color-teal-50: #F0FDFA;
  --color-teal-100: #CCFBF1;
  --color-teal-200: #99F6E4;
  --color-teal-300: #5EEAD4;
  --color-teal-400: #2DD4BF;
  --color-teal-500: #14B8A6;
  --color-teal-600: #0D9488;
  --color-teal-700: #0F766E;
  --color-teal-800: #115E59;
  --color-teal-900: #134E4A;
  --color-teal-950: #042F2E;

  /* Cyan */
  --color-cyan-50: #ECFEFF;
  --color-cyan-100: #CFFAFE;
  --color-cyan-200: #A5F3FC;
  --color-cyan-300: #67E8F9;
  --color-cyan-400: #22D3EE;
  --color-cyan-500: #06B6D4;
  --color-cyan-600: #0891B2;
  --color-cyan-700: #0E7490;
  --color-cyan-800: #155E75;
  --color-cyan-900: #164E63;
  --color-cyan-950: #083344;

  /* Sky */
  --color-sky-50: #F0F9FF;
  --color-sky-100: #E0F2FE;
  --color-sky-200: #BAE6FD;
  --color-sky-300: #7DD3FC;
  --color-sky-400: #38BDF8;
  --color-sky-500: #0EA5E9;
  --color-sky-600: #0284C7;
  --color-sky-700: #0369A1;
  --color-sky-800: #075985;
  --color-sky-900: #0C4A6E;
  --color-sky-950: #082F49;
}
```

### Semantic Color Tokens

```css
:root {
  /* Background */
  --color-bg-primary: var(--color-gray-50);
  --color-bg-secondary: white;
  --color-bg-tertiary: var(--color-gray-100);
  --color-bg-inverse: var(--color-gray-900);
  --color-bg-elevated: white;

  /* Surface (cards, modals) */
  --color-surface-primary: white;
  --color-surface-secondary: var(--color-gray-50);
  --color-surface-elevated: white;
  --color-surface-overlay: rgba(0, 0, 0, 0.5);

  /* Text */
  --color-text-primary: var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary: var(--color-gray-400);
  --color-text-inverse: white;
  --color-text-disabled: var(--color-gray-400);
  --color-text-placeholder: var(--color-gray-400);

  /* Border */
  --color-border-primary: var(--color-gray-200);
  --color-border-secondary: var(--color-gray-300);
  --color-border-focus: var(--color-blue-500);
  --color-border-error: var(--color-red-500);

  /* Interactive */
  --color-interactive-primary: var(--color-blue-600);
  --color-interactive-primary-hover: var(--color-blue-700);
  --color-interactive-primary-active: var(--color-blue-800);
  --color-interactive-secondary: var(--color-gray-600);
  --color-interactive-secondary-hover: var(--color-gray-700);

  /* Status */
  --color-success: var(--color-green-600);
  --color-success-light: var(--color-green-100);
  --color-success-dark: var(--color-green-800);
  
  --color-warning: var(--color-amber-500);
  --color-warning-light: var(--color-amber-100);
  --color-warning-dark: var(--color-amber-700);
  
  --color-error: var(--color-red-600);
  --color-error-light: var(--color-red-100);
  --color-error-dark: var(--color-red-800);
  
  --color-info: var(--color-blue-600);
  --color-info-light: var(--color-blue-100);
  --color-info-dark: var(--color-blue-800);

  /* Brand */
  --color-brand-primary: var(--color-blue-600);
  --color-brand-secondary: var(--color-indigo-600);
  --color-brand-accent: var(--color-amber-500);
}
```

### Dark Mode Tokens

```css
[data-theme="dark"] {
  /* Background */
  --color-bg-primary: var(--color-gray-950);
  --color-bg-secondary: var(--color-gray-900);
  --color-bg-tertiary: var(--color-gray-800);
  --color-bg-inverse: white;
  --color-bg-elevated: var(--color-gray-800);

  /* Surface */
  --color-surface-primary: var(--color-gray-900);
  --color-surface-secondary: var(--color-gray-800);
  --color-surface-elevated: var(--color-gray-800);
  --color-surface-overlay: rgba(0, 0, 0, 0.75);

  /* Text */
  --color-text-primary: var(--color-gray-50);
  --color-text-secondary: var(--color-gray-400);
  --color-text-tertiary: var(--color-gray-500);
  --color-text-inverse: var(--color-gray-900);
  --color-text-disabled: var(--color-gray-600);
  --color-text-placeholder: var(--color-gray-500);

  /* Border */
  --color-border-primary: var(--color-gray-700);
  --color-border-secondary: var(--color-gray-600);
}

/* Auto dark mode based on system preference */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* Same as [data-theme="dark"] */
  }
}
```

---

## Spacing Tokens

### Base Spacing Scale (8px Grid)

```css
:root {
  /* Primitive spacing */
  --space-0: 0;
  --space-px: 1px;
  --space-0-5: 2px;
  --space-1: 4px;
  --space-1-5: 6px;
  --space-2: 8px;
  --space-2-5: 10px;
  --space-3: 12px;
  --space-3-5: 14px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-7: 28px;
  --space-8: 32px;
  --space-9: 36px;
  --space-10: 40px;
  --space-11: 44px;
  --space-12: 48px;
  --space-14: 56px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-28: 112px;
  --space-32: 128px;
  --space-36: 144px;
  --space-40: 160px;
  --space-44: 176px;
  --space-48: 192px;
  --space-52: 208px;
  --space-56: 224px;
  --space-60: 240px;
  --space-64: 256px;
  --space-72: 288px;
  --space-80: 320px;
  --space-96: 384px;

  /* Semantic spacing */
  --spacing-none: var(--space-0);
  --spacing-xs: var(--space-1);      /* 4px */
  --spacing-sm: var(--space-2);      /* 8px */
  --spacing-md: var(--space-4);      /* 16px */
  --spacing-lg: var(--space-6);      /* 24px */
  --spacing-xl: var(--space-8);      /* 32px */
  --spacing-2xl: var(--space-12);    /* 48px */
  --spacing-3xl: var(--space-16);    /* 64px */
  --spacing-4xl: var(--space-24);    /* 96px */

  /* Component spacing */
  --spacing-inline-xs: var(--space-1);
  --spacing-inline-sm: var(--space-2);
  --spacing-inline-md: var(--space-3);
  --spacing-inline-lg: var(--space-4);

  --spacing-stack-xs: var(--space-2);
  --spacing-stack-sm: var(--space-4);
  --spacing-stack-md: var(--space-6);
  --spacing-stack-lg: var(--space-8);

  /* Layout spacing */
  --spacing-gutter: var(--space-6);
  --spacing-section: var(--space-16);
  --spacing-page: var(--space-24);
}
```

---

## Typography Tokens

### Font Family

```css
:root {
  --font-family-sans: 'Inter', ui-sans-serif, system-ui, -apple-system, 
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, 
    "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", 
    "Segoe UI Symbol", "Noto Color Emoji";
  
  --font-family-serif: ui-serif, Georgia, Cambria, "Times New Roman", 
    Times, serif;
  
  --font-family-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, 
    Consolas, "Liberation Mono", "Courier New", monospace;
  
  --font-family-display: 'Plus Jakarta Sans', var(--font-family-sans);
}
```

### Font Size

```css
:root {
  /* Primitive font sizes */
  --font-size-xs: 0.75rem;      /* 12px */
  --font-size-sm: 0.875rem;     /* 14px */
  --font-size-base: 1rem;       /* 16px */
  --font-size-lg: 1.125rem;     /* 18px */
  --font-size-xl: 1.25rem;      /* 20px */
  --font-size-2xl: 1.5rem;      /* 24px */
  --font-size-3xl: 1.875rem;    /* 30px */
  --font-size-4xl: 2.25rem;     /* 36px */
  --font-size-5xl: 3rem;        /* 48px */
  --font-size-6xl: 3.75rem;     /* 60px */
  --font-size-7xl: 4.5rem;      /* 72px */
  --font-size-8xl: 6rem;        /* 96px */
  --font-size-9xl: 8rem;        /* 128px */

  /* Semantic text sizes */
  --text-hero: var(--font-size-6xl);
  --text-display: var(--font-size-5xl);
  --text-h1: var(--font-size-4xl);
  --text-h2: var(--font-size-3xl);
  --text-h3: var(--font-size-2xl);
  --text-h4: var(--font-size-xl);
  --text-h5: var(--font-size-lg);
  --text-h6: var(--font-size-base);
  --text-body-lg: var(--font-size-lg);
  --text-body: var(--font-size-base);
  --text-body-sm: var(--font-size-sm);
  --text-caption: var(--font-size-xs);
  --text-overline: var(--font-size-xs);
}
```

### Font Weight

```css
:root {
  --font-weight-thin: 100;
  --font-weight-extralight: 200;
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;
  --font-weight-black: 900;
}
```

### Line Height

```css
:root {
  --line-height-none: 1;
  --line-height-tight: 1.25;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;

  /* Semantic */
  --line-height-heading: var(--line-height-tight);
  --line-height-body: var(--line-height-relaxed);
}
```

### Letter Spacing

```css
:root {
  --letter-spacing-tighter: -0.05em;
  --letter-spacing-tight: -0.025em;
  --letter-spacing-normal: 0em;
  --letter-spacing-wide: 0.025em;
  --letter-spacing-wider: 0.05em;
  --letter-spacing-widest: 0.1em;

  /* Semantic */
  --letter-spacing-heading: var(--letter-spacing-tight);
  --letter-spacing-body: var(--letter-spacing-normal);
  --letter-spacing-caps: var(--letter-spacing-wider);
}
```

---

## Border & Radius Tokens

### Border Width

```css
:root {
  --border-width-0: 0;
  --border-width-1: 1px;
  --border-width-2: 2px;
  --border-width-4: 4px;
  --border-width-8: 8px;

  /* Semantic */
  --border-width-default: var(--border-width-1);
  --border-width-focus: var(--border-width-2);
  --border-width-thick: var(--border-width-4);
}
```

### Border Radius

```css
:root {
  --radius-none: 0;
  --radius-sm: 0.125rem;    /* 2px */
  --radius-default: 0.25rem; /* 4px */
  --radius-md: 0.375rem;    /* 6px */
  --radius-lg: 0.5rem;      /* 8px */
  --radius-xl: 0.75rem;     /* 12px */
  --radius-2xl: 1rem;       /* 16px */
  --radius-3xl: 1.5rem;     /* 24px */
  --radius-full: 9999px;

  /* Semantic */
  --radius-button: var(--radius-lg);
  --radius-input: var(--radius-md);
  --radius-card: var(--radius-xl);
  --radius-modal: var(--radius-2xl);
  --radius-badge: var(--radius-full);
  --radius-avatar: var(--radius-full);
}
```

---

## Shadow Tokens

```css
:root {
  /* Primitive shadows */
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
  --shadow-none: none;

  /* Colored shadows */
  --shadow-primary: 0 4px 14px 0 rgb(59 130 246 / 0.3);
  --shadow-success: 0 4px 14px 0 rgb(34 197 94 / 0.3);
  --shadow-error: 0 4px 14px 0 rgb(239 68 68 / 0.3);

  /* Semantic shadows */
  --shadow-button: var(--shadow-sm);
  --shadow-button-hover: var(--shadow-md);
  --shadow-card: var(--shadow-md);
  --shadow-card-hover: var(--shadow-lg);
  --shadow-dropdown: var(--shadow-lg);
  --shadow-modal: var(--shadow-2xl);
  --shadow-tooltip: var(--shadow-md);
}
```

---

## Animation Tokens

### Duration

```css
:root {
  --duration-instant: 0ms;
  --duration-fast: 100ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --duration-slower: 400ms;
  --duration-slowest: 500ms;

  /* Semantic */
  --duration-hover: var(--duration-fast);
  --duration-focus: var(--duration-fast);
  --duration-active: var(--duration-instant);
  --duration-enter: var(--duration-normal);
  --duration-exit: var(--duration-fast);
  --duration-move: var(--duration-slow);
}
```

### Easing

```css
:root {
  --ease-linear: linear;
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  
  /* Expressive */
  --ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
  --ease-elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6);
  
  /* Standard (Material Design) */
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-decelerate: cubic-bezier(0, 0, 0.2, 1);
  --ease-accelerate: cubic-bezier(0.4, 0, 1, 1);

  /* Semantic */
  --ease-enter: var(--ease-out);
  --ease-exit: var(--ease-in);
  --ease-move: var(--ease-in-out);
}
```

---

## Z-Index Tokens

```css
:root {
  --z-hide: -1;
  --z-base: 0;
  --z-raised: 1;
  --z-dropdown: 1000;
  --z-sticky: 1100;
  --z-fixed: 1200;
  --z-overlay: 1300;
  --z-modal: 1400;
  --z-popover: 1500;
  --z-toast: 1600;
  --z-tooltip: 1700;
  --z-max: 9999;
}
```

---

## Breakpoint Tokens

```css
:root {
  --breakpoint-xs: 0;
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}

/* Usage in media queries */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

---

## Container Tokens

```css
:root {
  --container-xs: 320px;
  --container-sm: 384px;
  --container-md: 448px;
  --container-lg: 512px;
  --container-xl: 576px;
  --container-2xl: 672px;
  --container-3xl: 768px;
  --container-4xl: 896px;
  --container-5xl: 1024px;
  --container-6xl: 1152px;
  --container-7xl: 1280px;

  /* Common layout widths */
  --container-prose: 65ch;
  --container-content: var(--container-5xl);
  --container-wide: var(--container-7xl);
}
```

---

## Component Tokens (Examples)

### Button Tokens

```css
:root {
  /* Button base */
  --button-font-family: var(--font-family-sans);
  --button-font-weight: var(--font-weight-medium);
  --button-border-radius: var(--radius-lg);
  --button-transition: all var(--duration-fast) var(--ease-out);

  /* Button sizes */
  --button-height-xs: 28px;
  --button-height-sm: 32px;
  --button-height-md: 40px;
  --button-height-lg: 48px;
  --button-height-xl: 56px;

  --button-padding-x-xs: var(--space-2);
  --button-padding-x-sm: var(--space-3);
  --button-padding-x-md: var(--space-4);
  --button-padding-x-lg: var(--space-6);
  --button-padding-x-xl: var(--space-8);

  --button-font-size-xs: var(--font-size-xs);
  --button-font-size-sm: var(--font-size-sm);
  --button-font-size-md: var(--font-size-sm);
  --button-font-size-lg: var(--font-size-base);
  --button-font-size-xl: var(--font-size-lg);

  /* Button variants */
  --button-primary-bg: var(--color-interactive-primary);
  --button-primary-bg-hover: var(--color-interactive-primary-hover);
  --button-primary-text: white;
  
  --button-secondary-bg: var(--color-gray-100);
  --button-secondary-bg-hover: var(--color-gray-200);
  --button-secondary-text: var(--color-text-primary);
}
```

### Input Tokens

```css
:root {
  /* Input base */
  --input-font-family: var(--font-family-sans);
  --input-font-size: var(--font-size-base);
  --input-border-radius: var(--radius-md);
  --input-border-width: var(--border-width-1);
  --input-transition: all var(--duration-fast) var(--ease-out);

  /* Input heights */
  --input-height-sm: 32px;
  --input-height-md: 40px;
  --input-height-lg: 48px;

  /* Input colors */
  --input-bg: white;
  --input-bg-disabled: var(--color-gray-100);
  --input-border-color: var(--color-border-primary);
  --input-border-color-hover: var(--color-border-secondary);
  --input-border-color-focus: var(--color-border-focus);
  --input-border-color-error: var(--color-border-error);
  --input-text: var(--color-text-primary);
  --input-placeholder: var(--color-text-placeholder);

  /* Input focus ring */
  --input-focus-ring-width: 4px;
  --input-focus-ring-color: rgb(59 130 246 / 0.2);
  --input-focus-ring-color-error: rgb(239 68 68 / 0.2);
}
```

### Card Tokens

```css
:root {
  --card-bg: var(--color-surface-primary);
  --card-border-radius: var(--radius-xl);
  --card-padding: var(--space-6);
  --card-shadow: var(--shadow-md);
  --card-shadow-hover: var(--shadow-lg);
  --card-border-color: var(--color-border-primary);
  --card-transition: all var(--duration-normal) var(--ease-out);
}
```

---

## Token Export Formats

### JavaScript/TypeScript

```typescript
export const tokens = {
  color: {
    primary: {
      50: '#EFF6FF',
      500: '#3B82F6',
      600: '#2563EB',
      // ...
    },
    // ...
  },
  spacing: {
    0: '0',
    1: '4px',
    2: '8px',
    // ...
  },
  // ...
} as const;

export type ColorToken = keyof typeof tokens.color;
export type SpacingToken = keyof typeof tokens.spacing;
```

### Tailwind Config

```javascript
module.exports = {
  theme: {
    colors: {
      primary: {
        50: 'var(--color-blue-50)',
        500: 'var(--color-blue-500)',
        600: 'var(--color-blue-600)',
      },
      // Uses CSS variables for runtime theming
    },
    spacing: {
      0: 'var(--space-0)',
      1: 'var(--space-1)',
      2: 'var(--space-2)',
      // ...
    },
  },
};
```

### Figma Variables (JSON Export)

```json
{
  "color": {
    "primary": {
      "50": { "value": "#EFF6FF", "type": "color" },
      "500": { "value": "#3B82F6", "type": "color" },
      "600": { "value": "#2563EB", "type": "color" }
    }
  },
  "spacing": {
    "1": { "value": "4px", "type": "spacing" },
    "2": { "value": "8px", "type": "spacing" }
  }
}
```

---

This token system provides a complete foundation for building consistent, scalable design systems across any platform.
