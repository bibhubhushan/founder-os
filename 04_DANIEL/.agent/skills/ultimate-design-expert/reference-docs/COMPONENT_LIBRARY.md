# Component Library Reference

Complete specifications for production-ready UI components with code examples.

---

## Button Components

### Primary Button

```tsx
// React + Tailwind
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  isLoading?: boolean;
  isDisabled?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
  isFullWidth?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  isDisabled = false,
  leftIcon,
  rightIcon,
  isFullWidth = false,
  children,
  onClick,
}) => {
  const baseStyles = `
    inline-flex items-center justify-center
    font-medium rounded-lg
    transition-all duration-150 ease-out
    focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2
    disabled:opacity-50 disabled:cursor-not-allowed
  `;

  const variants = {
    primary: `
      bg-primary-600 text-white
      hover:bg-primary-700 active:bg-primary-800
      focus-visible:ring-primary-500
      shadow-sm hover:shadow
    `,
    secondary: `
      bg-gray-100 text-gray-900
      hover:bg-gray-200 active:bg-gray-300
      focus-visible:ring-gray-500
    `,
    outline: `
      border-2 border-gray-300 text-gray-700 bg-transparent
      hover:bg-gray-50 active:bg-gray-100
      focus-visible:ring-gray-500
    `,
    ghost: `
      text-gray-600 bg-transparent
      hover:bg-gray-100 active:bg-gray-200
      focus-visible:ring-gray-500
    `,
    danger: `
      bg-red-600 text-white
      hover:bg-red-700 active:bg-red-800
      focus-visible:ring-red-500
    `,
  };

  const sizes = {
    xs: 'px-2.5 py-1.5 text-xs gap-1',
    sm: 'px-3 py-2 text-sm gap-1.5',
    md: 'px-4 py-2.5 text-sm gap-2',
    lg: 'px-5 py-3 text-base gap-2',
    xl: 'px-6 py-4 text-lg gap-2.5',
  };

  return (
    <button
      className={`
        ${baseStyles}
        ${variants[variant]}
        ${sizes[size]}
        ${isFullWidth ? 'w-full' : ''}
      `}
      disabled={isDisabled || isLoading}
      onClick={onClick}
    >
      {isLoading ? (
        <Spinner className="w-4 h-4 animate-spin" />
      ) : (
        <>
          {leftIcon && <span className="shrink-0">{leftIcon}</span>}
          {children}
          {rightIcon && <span className="shrink-0">{rightIcon}</span>}
        </>
      )}
    </button>
  );
};
```

### Icon Button

```tsx
interface IconButtonProps {
  icon: React.ReactNode;
  'aria-label': string;
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isRound?: boolean;
}

const IconButton: React.FC<IconButtonProps> = ({
  icon,
  'aria-label': ariaLabel,
  variant = 'ghost',
  size = 'md',
  isRound = false,
}) => {
  const sizes = {
    sm: 'w-8 h-8',
    md: 'w-10 h-10',
    lg: 'w-12 h-12',
  };

  return (
    <button
      aria-label={ariaLabel}
      className={`
        ${sizes[size]}
        inline-flex items-center justify-center
        ${isRound ? 'rounded-full' : 'rounded-lg'}
        transition-colors duration-150
        hover:bg-gray-100 active:bg-gray-200
        focus:outline-none focus-visible:ring-2
      `}
    >
      {icon}
    </button>
  );
};
```

---

## Form Components

### Text Input

```tsx
interface InputProps {
  label?: string;
  placeholder?: string;
  helperText?: string;
  errorMessage?: string;
  isRequired?: boolean;
  isDisabled?: boolean;
  isReadOnly?: boolean;
  leftElement?: React.ReactNode;
  rightElement?: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
  type?: 'text' | 'email' | 'password' | 'number' | 'tel' | 'url';
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Input: React.FC<InputProps> = ({
  label,
  placeholder,
  helperText,
  errorMessage,
  isRequired = false,
  isDisabled = false,
  isReadOnly = false,
  leftElement,
  rightElement,
  size = 'md',
  type = 'text',
  value,
  onChange,
}) => {
  const isInvalid = !!errorMessage;
  
  const sizes = {
    sm: 'h-8 text-sm px-3',
    md: 'h-10 text-base px-4',
    lg: 'h-12 text-lg px-4',
  };

  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <label className="text-sm font-medium text-gray-700">
          {label}
          {isRequired && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      
      <div className="relative">
        {leftElement && (
          <div className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
            {leftElement}
          </div>
        )}
        
        <input
          type={type}
          value={value}
          onChange={onChange}
          placeholder={placeholder}
          disabled={isDisabled}
          readOnly={isReadOnly}
          required={isRequired}
          className={`
            w-full rounded-lg border
            ${sizes[size]}
            ${leftElement ? 'pl-10' : ''}
            ${rightElement ? 'pr-10' : ''}
            ${isInvalid 
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500/20' 
              : 'border-gray-300 focus:border-primary-500 focus:ring-primary-500/20'
            }
            ${isDisabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'}
            transition-all duration-150
            focus:outline-none focus:ring-4
          `}
        />
        
        {rightElement && (
          <div className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400">
            {rightElement}
          </div>
        )}
      </div>
      
      {(helperText || errorMessage) && (
        <p className={`text-sm ${isInvalid ? 'text-red-600' : 'text-gray-500'}`}>
          {errorMessage || helperText}
        </p>
      )}
    </div>
  );
};
```

### Textarea

```tsx
interface TextareaProps {
  label?: string;
  placeholder?: string;
  helperText?: string;
  errorMessage?: string;
  isRequired?: boolean;
  isDisabled?: boolean;
  rows?: number;
  maxLength?: number;
  showCount?: boolean;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
}

const Textarea: React.FC<TextareaProps> = ({
  label,
  placeholder,
  helperText,
  errorMessage,
  isRequired = false,
  isDisabled = false,
  rows = 4,
  maxLength,
  showCount = false,
  value = '',
  onChange,
}) => {
  const isInvalid = !!errorMessage;
  
  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <label className="text-sm font-medium text-gray-700">
          {label}
          {isRequired && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      
      <textarea
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        disabled={isDisabled}
        required={isRequired}
        rows={rows}
        maxLength={maxLength}
        className={`
          w-full rounded-lg border px-4 py-3
          resize-y min-h-[100px]
          ${isInvalid 
            ? 'border-red-500 focus:border-red-500 focus:ring-red-500/20' 
            : 'border-gray-300 focus:border-primary-500 focus:ring-primary-500/20'
          }
          ${isDisabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'}
          transition-all duration-150
          focus:outline-none focus:ring-4
        `}
      />
      
      <div className="flex justify-between">
        <p className={`text-sm ${isInvalid ? 'text-red-600' : 'text-gray-500'}`}>
          {errorMessage || helperText}
        </p>
        {showCount && maxLength && (
          <span className="text-sm text-gray-400">
            {value.length}/{maxLength}
          </span>
        )}
      </div>
    </div>
  );
};
```

### Select

```tsx
interface SelectProps {
  label?: string;
  placeholder?: string;
  options: Array<{ value: string; label: string; disabled?: boolean }>;
  helperText?: string;
  errorMessage?: string;
  isRequired?: boolean;
  isDisabled?: boolean;
  size?: 'sm' | 'md' | 'lg';
  value?: string;
  onChange?: (value: string) => void;
}

const Select: React.FC<SelectProps> = ({
  label,
  placeholder = 'Select an option',
  options,
  helperText,
  errorMessage,
  isRequired = false,
  isDisabled = false,
  size = 'md',
  value,
  onChange,
}) => {
  const isInvalid = !!errorMessage;
  
  const sizes = {
    sm: 'h-8 text-sm',
    md: 'h-10 text-base',
    lg: 'h-12 text-lg',
  };

  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <label className="text-sm font-medium text-gray-700">
          {label}
          {isRequired && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      
      <div className="relative">
        <select
          value={value}
          onChange={(e) => onChange?.(e.target.value)}
          disabled={isDisabled}
          required={isRequired}
          className={`
            w-full rounded-lg border px-4 pr-10
            ${sizes[size]}
            appearance-none cursor-pointer
            ${isInvalid 
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500/20' 
              : 'border-gray-300 focus:border-primary-500 focus:ring-primary-500/20'
            }
            ${isDisabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'}
            transition-all duration-150
            focus:outline-none focus:ring-4
          `}
        >
          <option value="" disabled>{placeholder}</option>
          {options.map((option) => (
            <option 
              key={option.value} 
              value={option.value}
              disabled={option.disabled}
            >
              {option.label}
            </option>
          ))}
        </select>
        
        {/* Chevron icon */}
        <div className="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none">
          <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </div>
      
      {(helperText || errorMessage) && (
        <p className={`text-sm ${isInvalid ? 'text-red-600' : 'text-gray-500'}`}>
          {errorMessage || helperText}
        </p>
      )}
    </div>
  );
};
```

### Checkbox

```tsx
interface CheckboxProps {
  label: string;
  description?: string;
  isChecked?: boolean;
  isIndeterminate?: boolean;
  isDisabled?: boolean;
  onChange?: (checked: boolean) => void;
}

const Checkbox: React.FC<CheckboxProps> = ({
  label,
  description,
  isChecked = false,
  isIndeterminate = false,
  isDisabled = false,
  onChange,
}) => {
  return (
    <label className={`
      flex items-start gap-3 cursor-pointer
      ${isDisabled ? 'opacity-50 cursor-not-allowed' : ''}
    `}>
      <div className="relative flex items-center justify-center">
        <input
          type="checkbox"
          checked={isChecked}
          disabled={isDisabled}
          onChange={(e) => onChange?.(e.target.checked)}
          className="peer sr-only"
        />
        <div className={`
          w-5 h-5 rounded border-2
          transition-all duration-150
          ${isChecked || isIndeterminate
            ? 'bg-primary-600 border-primary-600'
            : 'bg-white border-gray-300'
          }
          peer-focus-visible:ring-2 peer-focus-visible:ring-primary-500/50
          peer-hover:border-primary-400
        `}>
          {isChecked && (
            <svg className="w-full h-full text-white p-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
            </svg>
          )}
          {isIndeterminate && !isChecked && (
            <svg className="w-full h-full text-white p-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M20 12H4" />
            </svg>
          )}
        </div>
      </div>
      
      <div className="flex flex-col">
        <span className="text-sm font-medium text-gray-900">{label}</span>
        {description && (
          <span className="text-sm text-gray-500">{description}</span>
        )}
      </div>
    </label>
  );
};
```

### Radio Group

```tsx
interface RadioOption {
  value: string;
  label: string;
  description?: string;
  disabled?: boolean;
}

interface RadioGroupProps {
  name: string;
  label?: string;
  options: RadioOption[];
  value?: string;
  onChange?: (value: string) => void;
  orientation?: 'horizontal' | 'vertical';
}

const RadioGroup: React.FC<RadioGroupProps> = ({
  name,
  label,
  options,
  value,
  onChange,
  orientation = 'vertical',
}) => {
  return (
    <fieldset>
      {label && (
        <legend className="text-sm font-medium text-gray-700 mb-3">
          {label}
        </legend>
      )}
      
      <div className={`
        flex gap-4
        ${orientation === 'vertical' ? 'flex-col' : 'flex-row flex-wrap'}
      `}>
        {options.map((option) => (
          <label
            key={option.value}
            className={`
              flex items-start gap-3 cursor-pointer
              ${option.disabled ? 'opacity-50 cursor-not-allowed' : ''}
            `}
          >
            <div className="relative flex items-center justify-center mt-0.5">
              <input
                type="radio"
                name={name}
                value={option.value}
                checked={value === option.value}
                disabled={option.disabled}
                onChange={() => onChange?.(option.value)}
                className="peer sr-only"
              />
              <div className={`
                w-5 h-5 rounded-full border-2
                transition-all duration-150
                ${value === option.value
                  ? 'border-primary-600'
                  : 'border-gray-300'
                }
                peer-focus-visible:ring-2 peer-focus-visible:ring-primary-500/50
                peer-hover:border-primary-400
              `}>
                {value === option.value && (
                  <div className="w-full h-full flex items-center justify-center">
                    <div className="w-2.5 h-2.5 rounded-full bg-primary-600" />
                  </div>
                )}
              </div>
            </div>
            
            <div className="flex flex-col">
              <span className="text-sm font-medium text-gray-900">
                {option.label}
              </span>
              {option.description && (
                <span className="text-sm text-gray-500">
                  {option.description}
                </span>
              )}
            </div>
          </label>
        ))}
      </div>
    </fieldset>
  );
};
```

### Switch/Toggle

```tsx
interface SwitchProps {
  label?: string;
  description?: string;
  isChecked?: boolean;
  isDisabled?: boolean;
  size?: 'sm' | 'md' | 'lg';
  onChange?: (checked: boolean) => void;
}

const Switch: React.FC<SwitchProps> = ({
  label,
  description,
  isChecked = false,
  isDisabled = false,
  size = 'md',
  onChange,
}) => {
  const sizes = {
    sm: { track: 'w-8 h-4', thumb: 'w-3 h-3', translate: 'translate-x-4' },
    md: { track: 'w-11 h-6', thumb: 'w-5 h-5', translate: 'translate-x-5' },
    lg: { track: 'w-14 h-7', thumb: 'w-6 h-6', translate: 'translate-x-7' },
  };

  return (
    <label className={`
      inline-flex items-center gap-3 cursor-pointer
      ${isDisabled ? 'opacity-50 cursor-not-allowed' : ''}
    `}>
      <button
        type="button"
        role="switch"
        aria-checked={isChecked}
        disabled={isDisabled}
        onClick={() => onChange?.(!isChecked)}
        className={`
          ${sizes[size].track}
          relative rounded-full
          transition-colors duration-200
          focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500/50
          ${isChecked ? 'bg-primary-600' : 'bg-gray-200'}
        `}
      >
        <span
          className={`
            ${sizes[size].thumb}
            absolute top-0.5 left-0.5
            bg-white rounded-full shadow
            transition-transform duration-200
            ${isChecked ? sizes[size].translate : 'translate-x-0'}
          `}
        />
      </button>
      
      {(label || description) && (
        <div className="flex flex-col">
          {label && (
            <span className="text-sm font-medium text-gray-900">{label}</span>
          )}
          {description && (
            <span className="text-sm text-gray-500">{description}</span>
          )}
        </div>
      )}
    </label>
  );
};
```

---

## Card Components

### Basic Card

```tsx
interface CardProps {
  children: React.ReactNode;
  variant?: 'elevated' | 'outlined' | 'filled';
  padding?: 'none' | 'sm' | 'md' | 'lg';
  isHoverable?: boolean;
  isClickable?: boolean;
  onClick?: () => void;
}

const Card: React.FC<CardProps> = ({
  children,
  variant = 'elevated',
  padding = 'md',
  isHoverable = false,
  isClickable = false,
  onClick,
}) => {
  const variants = {
    elevated: 'bg-white shadow-md',
    outlined: 'bg-white border border-gray-200',
    filled: 'bg-gray-50',
  };

  const paddings = {
    none: '',
    sm: 'p-4',
    md: 'p-6',
    lg: 'p-8',
  };

  return (
    <div
      onClick={onClick}
      className={`
        rounded-xl
        ${variants[variant]}
        ${paddings[padding]}
        ${isHoverable ? 'hover:shadow-lg hover:-translate-y-1 transition-all duration-200' : ''}
        ${isClickable ? 'cursor-pointer' : ''}
      `}
    >
      {children}
    </div>
  );
};
```

### Media Card

```tsx
interface MediaCardProps {
  image: string;
  imageAlt: string;
  eyebrow?: string;
  title: string;
  description?: string;
  meta?: React.ReactNode;
  action?: React.ReactNode;
  aspectRatio?: 'video' | 'square' | 'wide';
}

const MediaCard: React.FC<MediaCardProps> = ({
  image,
  imageAlt,
  eyebrow,
  title,
  description,
  meta,
  action,
  aspectRatio = 'video',
}) => {
  const aspectRatios = {
    video: 'aspect-video',
    square: 'aspect-square',
    wide: 'aspect-[2/1]',
  };

  return (
    <div className="rounded-xl bg-white shadow-md overflow-hidden group">
      {/* Image */}
      <div className={`relative ${aspectRatios[aspectRatio]} overflow-hidden`}>
        <img
          src={image}
          alt={imageAlt}
          className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
        />
      </div>
      
      {/* Content */}
      <div className="p-5">
        {eyebrow && (
          <span className="text-xs font-semibold uppercase tracking-wider text-primary-600">
            {eyebrow}
          </span>
        )}
        
        <h3 className="mt-1 text-lg font-semibold text-gray-900 line-clamp-2">
          {title}
        </h3>
        
        {description && (
          <p className="mt-2 text-sm text-gray-600 line-clamp-3">
            {description}
          </p>
        )}
        
        {(meta || action) && (
          <div className="mt-4 flex items-center justify-between">
            {meta && <div className="text-sm text-gray-500">{meta}</div>}
            {action}
          </div>
        )}
      </div>
    </div>
  );
};
```

---

## Modal/Dialog

```tsx
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  description?: string;
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  children: React.ReactNode;
  footer?: React.ReactNode;
  closeOnOverlayClick?: boolean;
  closeOnEsc?: boolean;
}

const Modal: React.FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  description,
  size = 'md',
  children,
  footer,
  closeOnOverlayClick = true,
  closeOnEsc = true,
}) => {
  const sizes = {
    sm: 'max-w-md',
    md: 'max-w-lg',
    lg: 'max-w-2xl',
    xl: 'max-w-4xl',
    full: 'max-w-[calc(100vw-2rem)]',
  };

  // Handle ESC key
  useEffect(() => {
    if (!closeOnEsc) return;
    
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    
    window.addEventListener('keydown', handleEsc);
    return () => window.removeEventListener('keydown', handleEsc);
  }, [closeOnEsc, onClose]);

  // Lock body scroll
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50 backdrop-blur-sm animate-fadeIn"
        onClick={closeOnOverlayClick ? onClose : undefined}
      />
      
      {/* Modal */}
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? 'modal-title' : undefined}
        className={`
          relative w-full ${sizes[size]}
          bg-white rounded-2xl shadow-2xl
          animate-modalIn
          max-h-[calc(100vh-2rem)] flex flex-col
        `}
      >
        {/* Header */}
        {(title || description) && (
          <div className="px-6 pt-6 pb-4">
            {title && (
              <h2 id="modal-title" className="text-xl font-semibold text-gray-900">
                {title}
              </h2>
            )}
            {description && (
              <p className="mt-1 text-sm text-gray-500">{description}</p>
            )}
          </div>
        )}
        
        {/* Close button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 rounded-lg hover:bg-gray-100 transition-colors"
          aria-label="Close"
        >
          <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        
        {/* Body */}
        <div className="px-6 py-4 overflow-y-auto flex-1">
          {children}
        </div>
        
        {/* Footer */}
        {footer && (
          <div className="px-6 py-4 border-t border-gray-100 flex justify-end gap-3">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
};

// Animation keyframes (add to global CSS)
/*
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.95) translateY(-10px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.animate-fadeIn { animation: fadeIn 200ms ease-out; }
.animate-modalIn { animation: modalIn 200ms ease-out; }
*/
```

---

## Toast/Notification

```tsx
interface ToastProps {
  id: string;
  title?: string;
  description: string;
  status?: 'info' | 'success' | 'warning' | 'error';
  duration?: number;
  isClosable?: boolean;
  onClose: (id: string) => void;
}

const Toast: React.FC<ToastProps> = ({
  id,
  title,
  description,
  status = 'info',
  duration = 5000,
  isClosable = true,
  onClose,
}) => {
  const statusConfig = {
    info: {
      bg: 'bg-blue-50',
      border: 'border-blue-200',
      icon: 'text-blue-600',
      iconPath: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
    },
    success: {
      bg: 'bg-green-50',
      border: 'border-green-200',
      icon: 'text-green-600',
      iconPath: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z',
    },
    warning: {
      bg: 'bg-yellow-50',
      border: 'border-yellow-200',
      icon: 'text-yellow-600',
      iconPath: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z',
    },
    error: {
      bg: 'bg-red-50',
      border: 'border-red-200',
      icon: 'text-red-600',
      iconPath: 'M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z',
    },
  };

  const config = statusConfig[status];

  // Auto dismiss
  useEffect(() => {
    if (duration) {
      const timer = setTimeout(() => onClose(id), duration);
      return () => clearTimeout(timer);
    }
  }, [duration, id, onClose]);

  return (
    <div
      role="alert"
      className={`
        ${config.bg} ${config.border}
        border rounded-lg p-4 shadow-lg
        flex items-start gap-3
        animate-slideInRight
        max-w-md
      `}
    >
      {/* Icon */}
      <svg className={`w-5 h-5 shrink-0 ${config.icon}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={config.iconPath} />
      </svg>
      
      {/* Content */}
      <div className="flex-1 min-w-0">
        {title && (
          <p className="font-medium text-gray-900">{title}</p>
        )}
        <p className="text-sm text-gray-600">{description}</p>
      </div>
      
      {/* Close button */}
      {isClosable && (
        <button
          onClick={() => onClose(id)}
          className="shrink-0 p-1 rounded hover:bg-black/5 transition-colors"
          aria-label="Dismiss"
        >
          <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      )}
    </div>
  );
};

// Toast container (positioned fixed)
const ToastContainer: React.FC<{ toasts: ToastProps[] }> = ({ toasts }) => {
  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
      {toasts.map((toast) => (
        <Toast key={toast.id} {...toast} />
      ))}
    </div>
  );
};
```

---

## Avatar

```tsx
interface AvatarProps {
  src?: string;
  name: string;
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl' | '2xl';
  status?: 'online' | 'offline' | 'busy' | 'away';
}

const Avatar: React.FC<AvatarProps> = ({
  src,
  name,
  size = 'md',
  status,
}) => {
  const sizes = {
    xs: 'w-6 h-6 text-xs',
    sm: 'w-8 h-8 text-sm',
    md: 'w-10 h-10 text-base',
    lg: 'w-12 h-12 text-lg',
    xl: 'w-16 h-16 text-xl',
    '2xl': 'w-20 h-20 text-2xl',
  };

  const statusSizes = {
    xs: 'w-1.5 h-1.5',
    sm: 'w-2 h-2',
    md: 'w-2.5 h-2.5',
    lg: 'w-3 h-3',
    xl: 'w-4 h-4',
    '2xl': 'w-5 h-5',
  };

  const statusColors = {
    online: 'bg-green-500',
    offline: 'bg-gray-400',
    busy: 'bg-red-500',
    away: 'bg-yellow-500',
  };

  // Get initials
  const initials = name
    .split(' ')
    .map((n) => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);

  // Generate consistent color from name
  const colors = [
    'bg-red-500', 'bg-orange-500', 'bg-amber-500', 'bg-yellow-500',
    'bg-lime-500', 'bg-green-500', 'bg-emerald-500', 'bg-teal-500',
    'bg-cyan-500', 'bg-sky-500', 'bg-blue-500', 'bg-indigo-500',
    'bg-violet-500', 'bg-purple-500', 'bg-fuchsia-500', 'bg-pink-500',
  ];
  const colorIndex = name.charCodeAt(0) % colors.length;
  const bgColor = colors[colorIndex];

  return (
    <div className="relative inline-flex">
      {src ? (
        <img
          src={src}
          alt={name}
          className={`${sizes[size]} rounded-full object-cover`}
        />
      ) : (
        <div className={`
          ${sizes[size]} ${bgColor}
          rounded-full
          flex items-center justify-center
          font-medium text-white
        `}>
          {initials}
        </div>
      )}
      
      {status && (
        <span className={`
          absolute bottom-0 right-0
          ${statusSizes[size]} ${statusColors[status]}
          rounded-full border-2 border-white
        `} />
      )}
    </div>
  );
};

// Avatar Group
interface AvatarGroupProps {
  avatars: Array<{ src?: string; name: string }>;
  max?: number;
  size?: 'sm' | 'md' | 'lg';
}

const AvatarGroup: React.FC<AvatarGroupProps> = ({
  avatars,
  max = 4,
  size = 'md',
}) => {
  const visibleAvatars = avatars.slice(0, max);
  const remainingCount = avatars.length - max;

  const overlapClasses = {
    sm: '-ml-2',
    md: '-ml-3',
    lg: '-ml-4',
  };

  return (
    <div className="flex items-center">
      {visibleAvatars.map((avatar, index) => (
        <div
          key={index}
          className={`${index > 0 ? overlapClasses[size] : ''} ring-2 ring-white rounded-full`}
        >
          <Avatar {...avatar} size={size} />
        </div>
      ))}
      
      {remainingCount > 0 && (
        <div className={`
          ${overlapClasses[size]}
          ${size === 'sm' ? 'w-8 h-8 text-xs' : size === 'md' ? 'w-10 h-10 text-sm' : 'w-12 h-12 text-base'}
          rounded-full bg-gray-100
          flex items-center justify-center
          font-medium text-gray-600
          ring-2 ring-white
        `}>
          +{remainingCount}
        </div>
      )}
    </div>
  );
};
```

---

## Badge/Tag

```tsx
interface BadgeProps {
  children: React.ReactNode;
  variant?: 'solid' | 'subtle' | 'outline';
  colorScheme?: 'gray' | 'red' | 'orange' | 'yellow' | 'green' | 'blue' | 'purple' | 'pink';
  size?: 'sm' | 'md' | 'lg';
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
  isRemovable?: boolean;
  onRemove?: () => void;
}

const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'subtle',
  colorScheme = 'gray',
  size = 'md',
  leftIcon,
  rightIcon,
  isRemovable = false,
  onRemove,
}) => {
  const colorSchemes = {
    gray: {
      solid: 'bg-gray-600 text-white',
      subtle: 'bg-gray-100 text-gray-700',
      outline: 'border border-gray-300 text-gray-700',
    },
    red: {
      solid: 'bg-red-600 text-white',
      subtle: 'bg-red-100 text-red-700',
      outline: 'border border-red-300 text-red-700',
    },
    green: {
      solid: 'bg-green-600 text-white',
      subtle: 'bg-green-100 text-green-700',
      outline: 'border border-green-300 text-green-700',
    },
    blue: {
      solid: 'bg-blue-600 text-white',
      subtle: 'bg-blue-100 text-blue-700',
      outline: 'border border-blue-300 text-blue-700',
    },
    // ... other colors follow same pattern
  };

  const sizes = {
    sm: 'px-2 py-0.5 text-xs',
    md: 'px-2.5 py-1 text-sm',
    lg: 'px-3 py-1.5 text-base',
  };

  return (
    <span className={`
      inline-flex items-center gap-1
      rounded-full font-medium
      ${colorSchemes[colorScheme]?.[variant] || colorSchemes.gray[variant]}
      ${sizes[size]}
    `}>
      {leftIcon && <span className="shrink-0">{leftIcon}</span>}
      {children}
      {rightIcon && <span className="shrink-0">{rightIcon}</span>}
      {isRemovable && (
        <button
          onClick={onRemove}
          className="shrink-0 ml-1 hover:opacity-70 transition-opacity"
          aria-label="Remove"
        >
          <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      )}
    </span>
  );
};
```

---

## Skeleton Loading

```tsx
interface SkeletonProps {
  width?: string | number;
  height?: string | number;
  borderRadius?: string;
  className?: string;
}

const Skeleton: React.FC<SkeletonProps> = ({
  width,
  height,
  borderRadius = '4px',
  className = '',
}) => {
  return (
    <div
      className={`animate-pulse bg-gray-200 ${className}`}
      style={{
        width: typeof width === 'number' ? `${width}px` : width,
        height: typeof height === 'number' ? `${height}px` : height,
        borderRadius,
      }}
    />
  );
};

// Skeleton variants
const SkeletonText: React.FC<{ lines?: number; spacing?: number }> = ({
  lines = 3,
  spacing = 12,
}) => {
  return (
    <div className="space-y-3" style={{ gap: spacing }}>
      {Array.from({ length: lines }).map((_, i) => (
        <Skeleton
          key={i}
          height={16}
          width={i === lines - 1 ? '60%' : '100%'}
        />
      ))}
    </div>
  );
};

const SkeletonCircle: React.FC<{ size?: number }> = ({ size = 40 }) => {
  return <Skeleton width={size} height={size} borderRadius="50%" />;
};

// Card skeleton example
const SkeletonCard: React.FC = () => {
  return (
    <div className="rounded-xl bg-white shadow-md overflow-hidden p-5 space-y-4">
      <Skeleton height={200} borderRadius="8px" />
      <Skeleton height={20} width="30%" />
      <Skeleton height={24} width="80%" />
      <SkeletonText lines={2} />
      <div className="flex justify-between items-center pt-2">
        <Skeleton height={16} width={80} />
        <Skeleton height={36} width={100} borderRadius="20px" />
      </div>
    </div>
  );
};
```

---

## Tabs

```tsx
interface TabsProps {
  tabs: Array<{
    id: string;
    label: string;
    icon?: React.ReactNode;
    content: React.ReactNode;
    disabled?: boolean;
  }>;
  defaultTab?: string;
  variant?: 'line' | 'enclosed' | 'pills';
  size?: 'sm' | 'md' | 'lg';
  onChange?: (tabId: string) => void;
}

const Tabs: React.FC<TabsProps> = ({
  tabs,
  defaultTab,
  variant = 'line',
  size = 'md',
  onChange,
}) => {
  const [activeTab, setActiveTab] = useState(defaultTab || tabs[0]?.id);

  const handleTabChange = (tabId: string) => {
    setActiveTab(tabId);
    onChange?.(tabId);
  };

  const sizes = {
    sm: 'text-sm px-3 py-1.5',
    md: 'text-base px-4 py-2',
    lg: 'text-lg px-5 py-2.5',
  };

  const variants = {
    line: {
      list: 'border-b border-gray-200',
      tab: (isActive: boolean) => `
        ${sizes[size]}
        border-b-2 -mb-px
        ${isActive 
          ? 'border-primary-600 text-primary-600' 
          : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
        }
      `,
    },
    enclosed: {
      list: 'border-b border-gray-200',
      tab: (isActive: boolean) => `
        ${sizes[size]}
        rounded-t-lg border border-b-0
        ${isActive
          ? 'bg-white border-gray-200 text-primary-600 -mb-px'
          : 'bg-gray-50 border-transparent text-gray-500 hover:text-gray-700'
        }
      `,
    },
    pills: {
      list: 'gap-2',
      tab: (isActive: boolean) => `
        ${sizes[size]}
        rounded-full
        ${isActive
          ? 'bg-primary-600 text-white'
          : 'text-gray-600 hover:bg-gray-100'
        }
      `,
    },
  };

  return (
    <div>
      {/* Tab list */}
      <div
        role="tablist"
        className={`flex ${variants[variant].list}`}
      >
        {tabs.map((tab) => (
          <button
            key={tab.id}
            role="tab"
            aria-selected={activeTab === tab.id}
            aria-controls={`panel-${tab.id}`}
            disabled={tab.disabled}
            onClick={() => handleTabChange(tab.id)}
            className={`
              inline-flex items-center gap-2
              font-medium transition-all
              disabled:opacity-50 disabled:cursor-not-allowed
              ${variants[variant].tab(activeTab === tab.id)}
            `}
          >
            {tab.icon}
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab panels */}
      {tabs.map((tab) => (
        <div
          key={tab.id}
          role="tabpanel"
          id={`panel-${tab.id}`}
          hidden={activeTab !== tab.id}
          className="py-4"
        >
          {tab.content}
        </div>
      ))}
    </div>
  );
};
```

---

## Tooltip

```tsx
interface TooltipProps {
  content: React.ReactNode;
  children: React.ReactNode;
  placement?: 'top' | 'right' | 'bottom' | 'left';
  delay?: number;
}

const Tooltip: React.FC<TooltipProps> = ({
  content,
  children,
  placement = 'top',
  delay = 300,
}) => {
  const [isVisible, setIsVisible] = useState(false);
  const timeoutRef = useRef<NodeJS.Timeout>();

  const showTooltip = () => {
    timeoutRef.current = setTimeout(() => setIsVisible(true), delay);
  };

  const hideTooltip = () => {
    clearTimeout(timeoutRef.current);
    setIsVisible(false);
  };

  const placements = {
    top: 'bottom-full left-1/2 -translate-x-1/2 mb-2',
    right: 'left-full top-1/2 -translate-y-1/2 ml-2',
    bottom: 'top-full left-1/2 -translate-x-1/2 mt-2',
    left: 'right-full top-1/2 -translate-y-1/2 mr-2',
  };

  const arrows = {
    top: 'top-full left-1/2 -translate-x-1/2 border-t-gray-900',
    right: 'right-full top-1/2 -translate-y-1/2 border-r-gray-900',
    bottom: 'bottom-full left-1/2 -translate-x-1/2 border-b-gray-900',
    left: 'left-full top-1/2 -translate-y-1/2 border-l-gray-900',
  };

  return (
    <div
      className="relative inline-flex"
      onMouseEnter={showTooltip}
      onMouseLeave={hideTooltip}
      onFocus={showTooltip}
      onBlur={hideTooltip}
    >
      {children}
      
      {isVisible && (
        <div
          role="tooltip"
          className={`
            absolute z-50 ${placements[placement]}
            px-3 py-2
            bg-gray-900 text-white text-sm
            rounded-lg shadow-lg
            whitespace-nowrap
            animate-fadeIn
          `}
        >
          {content}
          {/* Arrow */}
          <div className={`
            absolute
            border-4 border-transparent
            ${arrows[placement]}
          `} />
        </div>
      )}
    </div>
  );
};
```

---

This component library provides production-ready, accessible components following best practices. Each component includes:
- TypeScript interfaces
- Multiple variants and sizes
- Proper ARIA attributes
- Keyboard navigation support
- Animation states
- Responsive design considerations
