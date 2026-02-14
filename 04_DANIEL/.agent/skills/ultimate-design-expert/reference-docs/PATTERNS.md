# UX Patterns Reference

Production-ready UX patterns with complete code implementations.

---

## Navigation Patterns

### Responsive Header Navigation

```tsx
interface NavItem {
  label: string;
  href: string;
  children?: NavItem[];
}

const navItems: NavItem[] = [
  { label: 'Products', href: '/products', children: [
    { label: 'Analytics', href: '/products/analytics' },
    { label: 'Automation', href: '/products/automation' },
    { label: 'Integrations', href: '/products/integrations' },
  ]},
  { label: 'Solutions', href: '/solutions' },
  { label: 'Pricing', href: '/pricing' },
  { label: 'Resources', href: '/resources' },
];

const Header: React.FC = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [openDropdown, setOpenDropdown] = useState<string | null>(null);

  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <a href="/" className="flex items-center gap-2">
            <Logo className="h-8 w-auto" />
            <span className="font-semibold text-xl">Brand</span>
          </a>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center gap-1">
            {navItems.map((item) => (
              <div
                key={item.label}
                className="relative"
                onMouseEnter={() => item.children && setOpenDropdown(item.label)}
                onMouseLeave={() => setOpenDropdown(null)}
              >
                <a
                  href={item.href}
                  className="px-4 py-2 text-gray-600 hover:text-gray-900 
                           rounded-lg hover:bg-gray-100 transition-colors
                           flex items-center gap-1"
                >
                  {item.label}
                  {item.children && (
                    <ChevronDownIcon className="w-4 h-4" />
                  )}
                </a>

                {/* Dropdown */}
                {item.children && openDropdown === item.label && (
                  <div className="absolute top-full left-0 pt-2">
                    <div className="bg-white rounded-xl shadow-xl border border-gray-200 
                                  py-2 min-w-[200px] animate-fadeIn">
                      {item.children.map((child) => (
                        <a
                          key={child.label}
                          href={child.href}
                          className="block px-4 py-2 text-gray-600 
                                   hover:text-gray-900 hover:bg-gray-50"
                        >
                          {child.label}
                        </a>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}
          </nav>

          {/* Desktop CTA */}
          <div className="hidden lg:flex items-center gap-4">
            <a href="/login" className="text-gray-600 hover:text-gray-900">
              Sign in
            </a>
            <a
              href="/signup"
              className="px-4 py-2 bg-primary-600 text-white rounded-lg
                       hover:bg-primary-700 transition-colors"
            >
              Get started
            </a>
          </div>

          {/* Mobile menu button */}
          <button
            className="lg:hidden p-2 rounded-lg hover:bg-gray-100"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label="Toggle menu"
          >
            {isMobileMenuOpen ? (
              <XIcon className="w-6 h-6" />
            ) : (
              <MenuIcon className="w-6 h-6" />
            )}
          </button>
        </div>
      </div>

      {/* Mobile Navigation */}
      {isMobileMenuOpen && (
        <div className="lg:hidden border-t border-gray-200 bg-white">
          <nav className="px-4 py-4 space-y-2">
            {navItems.map((item) => (
              <div key={item.label}>
                <a
                  href={item.href}
                  className="block px-4 py-3 text-gray-900 font-medium
                           rounded-lg hover:bg-gray-100"
                >
                  {item.label}
                </a>
                {item.children && (
                  <div className="ml-4 mt-1 space-y-1">
                    {item.children.map((child) => (
                      <a
                        key={child.label}
                        href={child.href}
                        className="block px-4 py-2 text-gray-600 
                                 rounded-lg hover:bg-gray-100"
                      >
                        {child.label}
                      </a>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </nav>
          <div className="px-4 py-4 border-t border-gray-200 space-y-3">
            <a
              href="/login"
              className="block w-full px-4 py-3 text-center text-gray-900
                       rounded-lg border border-gray-300 hover:bg-gray-50"
            >
              Sign in
            </a>
            <a
              href="/signup"
              className="block w-full px-4 py-3 text-center text-white
                       bg-primary-600 rounded-lg hover:bg-primary-700"
            >
              Get started
            </a>
          </div>
        </div>
      )}
    </header>
  );
};
```

### Bottom Tab Navigation (Mobile)

```tsx
interface TabItem {
  id: string;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  href: string;
  badge?: number;
}

const tabs: TabItem[] = [
  { id: 'home', label: 'Home', icon: HomeIcon, href: '/' },
  { id: 'search', label: 'Search', icon: SearchIcon, href: '/search' },
  { id: 'create', label: 'Create', icon: PlusCircleIcon, href: '/create' },
  { id: 'notifications', label: 'Alerts', icon: BellIcon, href: '/notifications', badge: 3 },
  { id: 'profile', label: 'Profile', icon: UserIcon, href: '/profile' },
];

const BottomNav: React.FC<{ currentPath: string }> = ({ currentPath }) => {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-50 
                    bg-white border-t border-gray-200
                    safe-area-inset-bottom">
      <div className="flex items-center justify-around h-16">
        {tabs.map((tab) => {
          const isActive = currentPath === tab.href;
          const Icon = tab.icon;

          return (
            <a
              key={tab.id}
              href={tab.href}
              className={`
                flex flex-col items-center justify-center
                w-full h-full gap-1
                transition-colors
                ${isActive ? 'text-primary-600' : 'text-gray-500'}
              `}
            >
              <div className="relative">
                <Icon className="w-6 h-6" />
                {tab.badge && (
                  <span className="absolute -top-1 -right-1 
                                 w-4 h-4 bg-red-500 text-white 
                                 text-xs rounded-full
                                 flex items-center justify-center">
                    {tab.badge}
                  </span>
                )}
              </div>
              <span className="text-xs font-medium">{tab.label}</span>
            </a>
          );
        })}
      </div>
    </nav>
  );
};
```

### Sidebar Navigation

```tsx
interface SidebarItem {
  id: string;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  href: string;
  badge?: string;
  children?: SidebarItem[];
}

const Sidebar: React.FC<{
  items: SidebarItem[];
  currentPath: string;
  isCollapsed?: boolean;
}> = ({ items, currentPath, isCollapsed = false }) => {
  const [expandedItems, setExpandedItems] = useState<string[]>([]);

  const toggleExpand = (id: string) => {
    setExpandedItems((prev) =>
      prev.includes(id)
        ? prev.filter((item) => item !== id)
        : [...prev, id]
    );
  };

  return (
    <aside
      className={`
        h-screen bg-gray-900 text-white
        transition-all duration-300
        ${isCollapsed ? 'w-16' : 'w-64'}
      `}
    >
      {/* Logo */}
      <div className="h-16 flex items-center px-4 border-b border-gray-800">
        {!isCollapsed && (
          <span className="font-semibold text-xl">Dashboard</span>
        )}
      </div>

      {/* Navigation */}
      <nav className="p-2 space-y-1">
        {items.map((item) => {
          const Icon = item.icon;
          const isActive = currentPath === item.href;
          const isExpanded = expandedItems.includes(item.id);
          const hasChildren = item.children && item.children.length > 0;

          return (
            <div key={item.id}>
              <a
                href={hasChildren ? '#' : item.href}
                onClick={(e) => {
                  if (hasChildren) {
                    e.preventDefault();
                    toggleExpand(item.id);
                  }
                }}
                className={`
                  flex items-center gap-3 px-3 py-2 rounded-lg
                  transition-colors
                  ${isActive
                    ? 'bg-primary-600 text-white'
                    : 'text-gray-400 hover:bg-gray-800 hover:text-white'
                  }
                `}
              >
                <Icon className="w-5 h-5 shrink-0" />
                {!isCollapsed && (
                  <>
                    <span className="flex-1">{item.label}</span>
                    {item.badge && (
                      <span className="px-2 py-0.5 text-xs bg-primary-500 rounded-full">
                        {item.badge}
                      </span>
                    )}
                    {hasChildren && (
                      <ChevronRightIcon
                        className={`w-4 h-4 transition-transform ${
                          isExpanded ? 'rotate-90' : ''
                        }`}
                      />
                    )}
                  </>
                )}
              </a>

              {/* Children */}
              {hasChildren && isExpanded && !isCollapsed && (
                <div className="mt-1 ml-4 pl-4 border-l border-gray-800 space-y-1">
                  {item.children!.map((child) => (
                    <a
                      key={child.id}
                      href={child.href}
                      className={`
                        block px-3 py-2 rounded-lg text-sm
                        ${currentPath === child.href
                          ? 'text-white bg-gray-800'
                          : 'text-gray-400 hover:text-white'
                        }
                      `}
                    >
                      {child.label}
                    </a>
                  ))}
                </div>
              )}
            </div>
          );
        })}
      </nav>
    </aside>
  );
};
```

---

## Form Patterns

### Multi-Step Form Wizard

```tsx
interface Step {
  id: string;
  title: string;
  description?: string;
  fields: React.ReactNode;
  validation?: () => boolean;
}

const FormWizard: React.FC<{
  steps: Step[];
  onComplete: (data: any) => void;
}> = ({ steps, onComplete }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState({});
  const [errors, setErrors] = useState<Record<string, string>>({});

  const isFirstStep = currentStep === 0;
  const isLastStep = currentStep === steps.length - 1;
  const step = steps[currentStep];

  const handleNext = () => {
    if (step.validation && !step.validation()) {
      return;
    }
    
    if (isLastStep) {
      onComplete(formData);
    } else {
      setCurrentStep((prev) => prev + 1);
    }
  };

  const handleBack = () => {
    setCurrentStep((prev) => prev - 1);
  };

  return (
    <div className="max-w-2xl mx-auto">
      {/* Progress indicator */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-2">
          {steps.map((s, index) => (
            <React.Fragment key={s.id}>
              {/* Step circle */}
              <div className="flex items-center">
                <div
                  className={`
                    w-10 h-10 rounded-full flex items-center justify-center
                    font-medium text-sm transition-colors
                    ${index < currentStep
                      ? 'bg-primary-600 text-white'
                      : index === currentStep
                      ? 'bg-primary-600 text-white ring-4 ring-primary-100'
                      : 'bg-gray-200 text-gray-500'
                    }
                  `}
                >
                  {index < currentStep ? (
                    <CheckIcon className="w-5 h-5" />
                  ) : (
                    index + 1
                  )}
                </div>
                {!isLastStep && index < steps.length - 1 && (
                  <div
                    className={`
                      hidden sm:block w-full h-1 mx-2
                      ${index < currentStep ? 'bg-primary-600' : 'bg-gray-200'}
                    `}
                    style={{ minWidth: '60px' }}
                  />
                )}
              </div>
            </React.Fragment>
          ))}
        </div>

        {/* Step labels */}
        <div className="hidden sm:flex justify-between">
          {steps.map((s, index) => (
            <span
              key={s.id}
              className={`
                text-sm
                ${index === currentStep
                  ? 'text-primary-600 font-medium'
                  : 'text-gray-500'
                }
              `}
            >
              {s.title}
            </span>
          ))}
        </div>
      </div>

      {/* Step content */}
      <div className="bg-white rounded-2xl shadow-lg p-8">
        <div className="mb-6">
          <h2 className="text-2xl font-semibold text-gray-900">
            {step.title}
          </h2>
          {step.description && (
            <p className="mt-1 text-gray-500">{step.description}</p>
          )}
        </div>

        <div className="space-y-6">{step.fields}</div>

        {/* Actions */}
        <div className="mt-8 flex justify-between">
          <button
            onClick={handleBack}
            disabled={isFirstStep}
            className={`
              px-6 py-2.5 rounded-lg font-medium
              ${isFirstStep
                ? 'invisible'
                : 'text-gray-700 hover:bg-gray-100'
              }
            `}
          >
            Back
          </button>

          <button
            onClick={handleNext}
            className="px-6 py-2.5 bg-primary-600 text-white rounded-lg
                     font-medium hover:bg-primary-700 transition-colors"
          >
            {isLastStep ? 'Complete' : 'Continue'}
          </button>
        </div>
      </div>
    </div>
  );
};
```

### Search with Autocomplete

```tsx
interface SearchResult {
  id: string;
  title: string;
  subtitle?: string;
  image?: string;
  type: string;
}

const SearchAutocomplete: React.FC<{
  onSearch: (query: string) => Promise<SearchResult[]>;
  onSelect: (result: SearchResult) => void;
  placeholder?: string;
}> = ({ onSearch, onSelect, placeholder = 'Search...' }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [highlightedIndex, setHighlightedIndex] = useState(-1);
  
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLUListElement>(null);

  // Debounced search
  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      return;
    }

    const timer = setTimeout(async () => {
      setIsLoading(true);
      try {
        const data = await onSearch(query);
        setResults(data);
        setIsOpen(true);
      } finally {
        setIsLoading(false);
      }
    }, 300);

    return () => clearTimeout(timer);
  }, [query, onSearch]);

  // Keyboard navigation
  const handleKeyDown = (e: React.KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setHighlightedIndex((prev) =>
          prev < results.length - 1 ? prev + 1 : prev
        );
        break;
      case 'ArrowUp':
        e.preventDefault();
        setHighlightedIndex((prev) => (prev > 0 ? prev - 1 : -1));
        break;
      case 'Enter':
        if (highlightedIndex >= 0) {
          onSelect(results[highlightedIndex]);
          setIsOpen(false);
          setQuery('');
        }
        break;
      case 'Escape':
        setIsOpen(false);
        inputRef.current?.blur();
        break;
    }
  };

  return (
    <div className="relative w-full max-w-lg">
      {/* Search input */}
      <div className="relative">
        <SearchIcon className="absolute left-4 top-1/2 -translate-y-1/2 
                              w-5 h-5 text-gray-400" />
        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => results.length > 0 && setIsOpen(true)}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          className="w-full h-12 pl-12 pr-4 
                   bg-gray-100 border-0 rounded-xl
                   text-gray-900 placeholder-gray-500
                   focus:bg-white focus:ring-2 focus:ring-primary-500
                   transition-all"
        />
        {isLoading && (
          <Spinner className="absolute right-4 top-1/2 -translate-y-1/2 
                             w-5 h-5 text-gray-400" />
        )}
      </div>

      {/* Results dropdown */}
      {isOpen && results.length > 0 && (
        <ul
          ref={listRef}
          className="absolute top-full left-0 right-0 mt-2
                   bg-white rounded-xl shadow-xl border border-gray-200
                   max-h-96 overflow-y-auto z-50"
          role="listbox"
        >
          {results.map((result, index) => (
            <li
              key={result.id}
              role="option"
              aria-selected={index === highlightedIndex}
              onClick={() => {
                onSelect(result);
                setIsOpen(false);
                setQuery('');
              }}
              onMouseEnter={() => setHighlightedIndex(index)}
              className={`
                flex items-center gap-4 px-4 py-3 cursor-pointer
                ${index === highlightedIndex ? 'bg-gray-100' : ''}
              `}
            >
              {result.image && (
                <img
                  src={result.image}
                  alt=""
                  className="w-10 h-10 rounded-lg object-cover"
                />
              )}
              <div className="flex-1 min-w-0">
                <p className="font-medium text-gray-900 truncate">
                  {result.title}
                </p>
                {result.subtitle && (
                  <p className="text-sm text-gray-500 truncate">
                    {result.subtitle}
                  </p>
                )}
              </div>
              <span className="text-xs text-gray-400 uppercase">
                {result.type}
              </span>
            </li>
          ))}
        </ul>
      )}

      {/* Empty state */}
      {isOpen && query && !isLoading && results.length === 0 && (
        <div className="absolute top-full left-0 right-0 mt-2
                      bg-white rounded-xl shadow-xl border border-gray-200
                      p-8 text-center">
          <p className="text-gray-500">No results found for "{query}"</p>
        </div>
      )}
    </div>
  );
};
```

### Inline Validation Form

```tsx
interface FieldConfig {
  name: string;
  label: string;
  type: 'text' | 'email' | 'password' | 'tel';
  placeholder?: string;
  required?: boolean;
  validate?: (value: string) => string | null;
}

const InlineValidationForm: React.FC<{
  fields: FieldConfig[];
  onSubmit: (data: Record<string, string>) => void;
}> = ({ fields, onSubmit }) => {
  const [values, setValues] = useState<Record<string, string>>({});
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});

  const validateField = (field: FieldConfig, value: string): string | null => {
    if (field.required && !value.trim()) {
      return `${field.label} is required`;
    }
    if (field.validate) {
      return field.validate(value);
    }
    if (field.type === 'email' && value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(value)) {
        return 'Please enter a valid email';
      }
    }
    return null;
  };

  const handleChange = (field: FieldConfig, value: string) => {
    setValues((prev) => ({ ...prev, [field.name]: value }));
    
    // Clear error when user starts typing
    if (errors[field.name]) {
      setErrors((prev) => ({ ...prev, [field.name]: '' }));
    }
  };

  const handleBlur = (field: FieldConfig) => {
    setTouched((prev) => ({ ...prev, [field.name]: true }));
    
    const error = validateField(field, values[field.name] || '');
    setErrors((prev) => ({ ...prev, [field.name]: error || '' }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validate all fields
    const newErrors: Record<string, string> = {};
    let hasErrors = false;
    
    fields.forEach((field) => {
      const error = validateField(field, values[field.name] || '');
      if (error) {
        newErrors[field.name] = error;
        hasErrors = true;
      }
    });
    
    setErrors(newErrors);
    setTouched(
      fields.reduce((acc, field) => ({ ...acc, [field.name]: true }), {})
    );
    
    if (!hasErrors) {
      onSubmit(values);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {fields.map((field) => {
        const value = values[field.name] || '';
        const error = errors[field.name];
        const isTouched = touched[field.name];
        const isValid = isTouched && !error && value;

        return (
          <div key={field.name}>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {field.label}
              {field.required && <span className="text-red-500 ml-1">*</span>}
            </label>
            
            <div className="relative">
              <input
                type={field.type}
                value={value}
                onChange={(e) => handleChange(field, e.target.value)}
                onBlur={() => handleBlur(field)}
                placeholder={field.placeholder}
                className={`
                  w-full px-4 py-3 rounded-lg border
                  transition-all duration-150
                  focus:outline-none focus:ring-4
                  ${error
                    ? 'border-red-500 focus:border-red-500 focus:ring-red-500/20'
                    : isValid
                    ? 'border-green-500 focus:border-green-500 focus:ring-green-500/20'
                    : 'border-gray-300 focus:border-primary-500 focus:ring-primary-500/20'
                  }
                `}
              />
              
              {/* Status icon */}
              <div className="absolute right-3 top-1/2 -translate-y-1/2">
                {error && (
                  <ExclamationCircleIcon className="w-5 h-5 text-red-500" />
                )}
                {isValid && (
                  <CheckCircleIcon className="w-5 h-5 text-green-500" />
                )}
              </div>
            </div>
            
            {/* Error message */}
            {error && (
              <p className="mt-1 text-sm text-red-600 flex items-center gap-1">
                {error}
              </p>
            )}
          </div>
        );
      })}

      <button
        type="submit"
        className="w-full py-3 bg-primary-600 text-white rounded-lg
                 font-medium hover:bg-primary-700 transition-colors"
      >
        Submit
      </button>
    </form>
  );
};
```

---

## Data Display Patterns

### Infinite Scroll List

```tsx
interface Item {
  id: string;
  [key: string]: any;
}

const InfiniteScrollList: React.FC<{
  fetchItems: (page: number) => Promise<{ items: Item[]; hasMore: boolean }>;
  renderItem: (item: Item) => React.ReactNode;
  itemKey: (item: Item) => string;
}> = ({ fetchItems, renderItem, itemKey }) => {
  const [items, setItems] = useState<Item[]>([]);
  const [page, setPage] = useState(1);
  const [isLoading, setIsLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  const observerRef = useRef<IntersectionObserver | null>(null);
  const loadMoreRef = useRef<HTMLDivElement>(null);

  // Initial load
  useEffect(() => {
    loadItems(1);
  }, []);

  // Setup intersection observer
  useEffect(() => {
    observerRef.current = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && hasMore && !isLoading) {
          loadItems(page + 1);
        }
      },
      { threshold: 0.1 }
    );

    if (loadMoreRef.current) {
      observerRef.current.observe(loadMoreRef.current);
    }

    return () => observerRef.current?.disconnect();
  }, [hasMore, isLoading, page]);

  const loadItems = async (pageNum: number) => {
    if (isLoading) return;
    
    setIsLoading(true);
    setError(null);
    
    try {
      const { items: newItems, hasMore: more } = await fetchItems(pageNum);
      setItems((prev) => (pageNum === 1 ? newItems : [...prev, ...newItems]));
      setPage(pageNum);
      setHasMore(more);
    } catch (err) {
      setError('Failed to load items. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      {/* Items list */}
      <div className="space-y-4">
        {items.map((item) => (
          <div key={itemKey(item)}>{renderItem(item)}</div>
        ))}
      </div>

      {/* Loading indicator */}
      {isLoading && (
        <div className="py-8 flex justify-center">
          <Spinner className="w-8 h-8 text-primary-600" />
        </div>
      )}

      {/* Error state */}
      {error && (
        <div className="py-8 text-center">
          <p className="text-red-600 mb-4">{error}</p>
          <button
            onClick={() => loadItems(page)}
            className="px-4 py-2 bg-primary-600 text-white rounded-lg"
          >
            Retry
          </button>
        </div>
      )}

      {/* Load more trigger */}
      {hasMore && !isLoading && !error && (
        <div ref={loadMoreRef} className="h-20" />
      )}

      {/* End of list */}
      {!hasMore && items.length > 0 && (
        <p className="py-8 text-center text-gray-500">
          You've reached the end
        </p>
      )}

      {/* Empty state */}
      {!isLoading && items.length === 0 && (
        <div className="py-16 text-center">
          <p className="text-gray-500">No items found</p>
        </div>
      )}
    </div>
  );
};
```

### Data Table with Sorting & Filtering

```tsx
interface Column<T> {
  key: keyof T;
  label: string;
  sortable?: boolean;
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface DataTableProps<T> {
  data: T[];
  columns: Column<T>[];
  searchable?: boolean;
  searchKeys?: (keyof T)[];
  pageSize?: number;
}

function DataTable<T extends { id: string }>({
  data,
  columns,
  searchable = true,
  searchKeys = [],
  pageSize = 10,
}: DataTableProps<T>) {
  const [search, setSearch] = useState('');
  const [sortKey, setSortKey] = useState<keyof T | null>(null);
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
  const [currentPage, setCurrentPage] = useState(1);

  // Filter data
  const filteredData = useMemo(() => {
    if (!search.trim()) return data;
    
    const searchLower = search.toLowerCase();
    return data.filter((row) =>
      searchKeys.some((key) =>
        String(row[key]).toLowerCase().includes(searchLower)
      )
    );
  }, [data, search, searchKeys]);

  // Sort data
  const sortedData = useMemo(() => {
    if (!sortKey) return filteredData;
    
    return [...filteredData].sort((a, b) => {
      const aVal = a[sortKey];
      const bVal = b[sortKey];
      
      if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  }, [filteredData, sortKey, sortDirection]);

  // Paginate data
  const paginatedData = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return sortedData.slice(start, start + pageSize);
  }, [sortedData, currentPage, pageSize]);

  const totalPages = Math.ceil(sortedData.length / pageSize);

  const handleSort = (key: keyof T) => {
    if (sortKey === key) {
      setSortDirection((prev) => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortKey(key);
      setSortDirection('asc');
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200">
      {/* Search */}
      {searchable && (
        <div className="p-4 border-b border-gray-200">
          <div className="relative max-w-md">
            <SearchIcon className="absolute left-3 top-1/2 -translate-y-1/2 
                                  w-5 h-5 text-gray-400" />
            <input
              type="text"
              value={search}
              onChange={(e) => {
                setSearch(e.target.value);
                setCurrentPage(1);
              }}
              placeholder="Search..."
              className="w-full pl-10 pr-4 py-2 border border-gray-300 
                       rounded-lg focus:ring-2 focus:ring-primary-500"
            />
          </div>
        </div>
      )}

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-50 border-b border-gray-200">
            <tr>
              {columns.map((column) => (
                <th
                  key={String(column.key)}
                  onClick={() => column.sortable && handleSort(column.key)}
                  className={`
                    px-6 py-3 text-left text-xs font-semibold 
                    text-gray-600 uppercase tracking-wider
                    ${column.sortable ? 'cursor-pointer hover:bg-gray-100' : ''}
                  `}
                >
                  <div className="flex items-center gap-2">
                    {column.label}
                    {column.sortable && sortKey === column.key && (
                      <span>
                        {sortDirection === 'asc' ? '↑' : '↓'}
                      </span>
                    )}
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {paginatedData.map((row) => (
              <tr key={row.id} className="hover:bg-gray-50">
                {columns.map((column) => (
                  <td
                    key={String(column.key)}
                    className="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
                  >
                    {column.render
                      ? column.render(row[column.key], row)
                      : String(row[column.key])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Pagination */}
      <div className="px-6 py-4 border-t border-gray-200 
                    flex items-center justify-between">
        <p className="text-sm text-gray-600">
          Showing {(currentPage - 1) * pageSize + 1} to{' '}
          {Math.min(currentPage * pageSize, sortedData.length)} of{' '}
          {sortedData.length} results
        </p>
        
        <div className="flex items-center gap-2">
          <button
            onClick={() => setCurrentPage((p) => p - 1)}
            disabled={currentPage === 1}
            className="px-3 py-1 rounded border border-gray-300
                     disabled:opacity-50 disabled:cursor-not-allowed
                     hover:bg-gray-50"
          >
            Previous
          </button>
          
          {Array.from({ length: totalPages }, (_, i) => i + 1)
            .filter((p) => 
              p === 1 || 
              p === totalPages || 
              Math.abs(p - currentPage) <= 1
            )
            .map((p, i, arr) => (
              <React.Fragment key={p}>
                {i > 0 && arr[i - 1] !== p - 1 && (
                  <span className="px-2">...</span>
                )}
                <button
                  onClick={() => setCurrentPage(p)}
                  className={`
                    w-8 h-8 rounded
                    ${p === currentPage
                      ? 'bg-primary-600 text-white'
                      : 'hover:bg-gray-100'
                    }
                  `}
                >
                  {p}
                </button>
              </React.Fragment>
            ))}
          
          <button
            onClick={() => setCurrentPage((p) => p + 1)}
            disabled={currentPage === totalPages}
            className="px-3 py-1 rounded border border-gray-300
                     disabled:opacity-50 disabled:cursor-not-allowed
                     hover:bg-gray-50"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
```

---

## Feedback Patterns

### Toast Notification System

```tsx
type ToastType = 'success' | 'error' | 'warning' | 'info';

interface Toast {
  id: string;
  type: ToastType;
  title?: string;
  message: string;
  duration?: number;
}

// Toast Context
const ToastContext = createContext<{
  addToast: (toast: Omit<Toast, 'id'>) => void;
  removeToast: (id: string) => void;
} | null>(null);

// Toast Provider
const ToastProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [toasts, setToasts] = useState<Toast[]>([]);

  const addToast = useCallback((toast: Omit<Toast, 'id'>) => {
    const id = Math.random().toString(36).substr(2, 9);
    setToasts((prev) => [...prev, { ...toast, id }]);
  }, []);

  const removeToast = useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  return (
    <ToastContext.Provider value={{ addToast, removeToast }}>
      {children}
      <ToastContainer toasts={toasts} onRemove={removeToast} />
    </ToastContext.Provider>
  );
};

// Toast Container
const ToastContainer: React.FC<{
  toasts: Toast[];
  onRemove: (id: string) => void;
}> = ({ toasts, onRemove }) => {
  return (
    <div className="fixed bottom-4 right-4 z-50 space-y-2">
      {toasts.map((toast) => (
        <ToastItem key={toast.id} toast={toast} onRemove={onRemove} />
      ))}
    </div>
  );
};

// Toast Item
const ToastItem: React.FC<{
  toast: Toast;
  onRemove: (id: string) => void;
}> = ({ toast, onRemove }) => {
  const { id, type, title, message, duration = 5000 } = toast;

  useEffect(() => {
    const timer = setTimeout(() => onRemove(id), duration);
    return () => clearTimeout(timer);
  }, [id, duration, onRemove]);

  const icons = {
    success: <CheckCircleIcon className="w-5 h-5 text-green-500" />,
    error: <XCircleIcon className="w-5 h-5 text-red-500" />,
    warning: <ExclamationIcon className="w-5 h-5 text-yellow-500" />,
    info: <InformationCircleIcon className="w-5 h-5 text-blue-500" />,
  };

  const colors = {
    success: 'bg-green-50 border-green-200',
    error: 'bg-red-50 border-red-200',
    warning: 'bg-yellow-50 border-yellow-200',
    info: 'bg-blue-50 border-blue-200',
  };

  return (
    <div
      className={`
        ${colors[type]}
        border rounded-lg shadow-lg p-4
        flex items-start gap-3
        min-w-[320px] max-w-md
        animate-slideInRight
      `}
    >
      {icons[type]}
      <div className="flex-1">
        {title && <p className="font-medium text-gray-900">{title}</p>}
        <p className="text-sm text-gray-600">{message}</p>
      </div>
      <button
        onClick={() => onRemove(id)}
        className="p-1 hover:bg-black/5 rounded"
      >
        <XIcon className="w-4 h-4 text-gray-400" />
      </button>
    </div>
  );
};

// Hook
const useToast = () => {
  const context = useContext(ToastContext);
  if (!context) throw new Error('useToast must be used within ToastProvider');
  return context;
};

// Usage
const ExampleComponent = () => {
  const { addToast } = useToast();

  const handleSuccess = () => {
    addToast({
      type: 'success',
      title: 'Success!',
      message: 'Your changes have been saved.',
    });
  };

  return <button onClick={handleSuccess}>Save</button>;
};
```

### Confirmation Dialog

```tsx
interface ConfirmDialogProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
  variant?: 'danger' | 'warning' | 'default';
  isLoading?: boolean;
}

const ConfirmDialog: React.FC<ConfirmDialogProps> = ({
  isOpen,
  onClose,
  onConfirm,
  title,
  message,
  confirmText = 'Confirm',
  cancelText = 'Cancel',
  variant = 'default',
  isLoading = false,
}) => {
  if (!isOpen) return null;

  const variants = {
    danger: {
      icon: <ExclamationIcon className="w-6 h-6 text-red-600" />,
      iconBg: 'bg-red-100',
      button: 'bg-red-600 hover:bg-red-700',
    },
    warning: {
      icon: <ExclamationIcon className="w-6 h-6 text-yellow-600" />,
      iconBg: 'bg-yellow-100',
      button: 'bg-yellow-600 hover:bg-yellow-700',
    },
    default: {
      icon: <QuestionMarkCircleIcon className="w-6 h-6 text-primary-600" />,
      iconBg: 'bg-primary-100',
      button: 'bg-primary-600 hover:bg-primary-700',
    },
  };

  const config = variants[variant];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Dialog */}
      <div className="relative bg-white rounded-2xl shadow-2xl max-w-md w-full p-6">
        <div className="flex items-start gap-4">
          {/* Icon */}
          <div className={`${config.iconBg} p-3 rounded-full shrink-0`}>
            {config.icon}
          </div>

          {/* Content */}
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
            <p className="mt-2 text-gray-600">{message}</p>
          </div>
        </div>

        {/* Actions */}
        <div className="mt-6 flex justify-end gap-3">
          <button
            onClick={onClose}
            disabled={isLoading}
            className="px-4 py-2 text-gray-700 hover:bg-gray-100 
                     rounded-lg font-medium transition-colors"
          >
            {cancelText}
          </button>
          <button
            onClick={onConfirm}
            disabled={isLoading}
            className={`
              px-4 py-2 text-white rounded-lg font-medium
              transition-colors disabled:opacity-50
              ${config.button}
            `}
          >
            {isLoading ? <Spinner className="w-5 h-5" /> : confirmText}
          </button>
        </div>
      </div>
    </div>
  );
};
```

---

## Empty States

```tsx
interface EmptyStateProps {
  icon?: React.ReactNode;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
  };
  secondaryAction?: {
    label: string;
    onClick: () => void;
  };
}

const EmptyState: React.FC<EmptyStateProps> = ({
  icon,
  title,
  description,
  action,
  secondaryAction,
}) => {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      {/* Icon/Illustration */}
      {icon && (
        <div className="w-16 h-16 bg-gray-100 rounded-full 
                      flex items-center justify-center mb-6">
          {icon}
        </div>
      )}

      {/* Text */}
      <h3 className="text-lg font-semibold text-gray-900 text-center">
        {title}
      </h3>
      {description && (
        <p className="mt-2 text-gray-500 text-center max-w-sm">
          {description}
        </p>
      )}

      {/* Actions */}
      {(action || secondaryAction) && (
        <div className="mt-6 flex items-center gap-4">
          {secondaryAction && (
            <button
              onClick={secondaryAction.onClick}
              className="px-4 py-2 text-gray-700 hover:bg-gray-100 
                       rounded-lg font-medium transition-colors"
            >
              {secondaryAction.label}
            </button>
          )}
          {action && (
            <button
              onClick={action.onClick}
              className="px-4 py-2 bg-primary-600 text-white 
                       rounded-lg font-medium hover:bg-primary-700 
                       transition-colors"
            >
              {action.label}
            </button>
          )}
        </div>
      )}
    </div>
  );
};

// Usage examples
const EmptyStateExamples = () => (
  <>
    {/* No results */}
    <EmptyState
      icon={<SearchIcon className="w-8 h-8 text-gray-400" />}
      title="No results found"
      description="Try adjusting your search or filters to find what you're looking for."
      action={{ label: 'Clear filters', onClick: () => {} }}
    />

    {/* First use */}
    <EmptyState
      icon={<PlusIcon className="w-8 h-8 text-gray-400" />}
      title="No projects yet"
      description="Create your first project to get started with your work."
      action={{ label: 'Create project', onClick: () => {} }}
      secondaryAction={{ label: 'Learn more', onClick: () => {} }}
    />

    {/* Error */}
    <EmptyState
      icon={<ExclamationCircleIcon className="w-8 h-8 text-red-500" />}
      title="Something went wrong"
      description="We couldn't load your data. Please try again."
      action={{ label: 'Retry', onClick: () => {} }}
    />
  </>
);
```

---

This patterns reference provides production-ready implementations for common UX patterns. Each pattern includes complete TypeScript code with proper typing, accessibility considerations, and responsive design.
