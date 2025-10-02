class SlidePresentation {
  constructor() {
    this.currentSlide = 1;
    this.totalSlides = 23;
    this.slidesWrapper = document.getElementById('slides-wrapper');
    this.progressFill = document.getElementById('progress-fill');
    this.slideCounter = document.getElementById('slide-counter');
    this.prevBtn = document.getElementById('prev-btn');
    this.nextBtn = document.getElementById('next-btn');

    this.init();
  }

  init() {
    this.setupEventListeners();
    this.updateSlideDisplay();
    this.updateNavigationButtons();
    this.updateProgressBar();
    this.updateSlideCounter();
    console.log('Apresentação inicializada com sucesso!');
  }

  setupEventListeners() {
    // Navigation buttons
    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.previousSlide();
      });
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.nextSlide();
      });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      switch(e.key) {
        case 'ArrowLeft':
        case 'ArrowUp':
        case 'PageUp':
          e.preventDefault();
          this.previousSlide();
          break;
        case 'ArrowRight':
        case 'ArrowDown':
        case 'PageDown':
        case ' ':
          e.preventDefault();
          this.nextSlide();
          break;
        case 'Home':
          e.preventDefault();
          this.goToSlide(1);
          break;
        case 'End':
          e.preventDefault();
          this.goToSlide(this.totalSlides);
          break;
        case 'Escape':
          if (document.fullscreenElement) {
            document.exitFullscreen();
          }
          break;
      }

      // Number keys for direct navigation (1-9)
      if (e.key >= '1' && e.key <= '9') {
        const slideNum = parseInt(e.key);
        if (slideNum <= this.totalSlides) {
          this.goToSlide(slideNum);
        }
      }
    });

    // Touch/swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    let touchStartY = 0;
    let touchEndY = 0;

    document.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      touchEndY = e.changedTouches[0].screenY;
      this.handleSwipe();
    }, { passive: true });

    const handleSwipe = () => {
      const swipeThreshold = 50;
      const diffX = touchStartX - touchEndX;
      const diffY = touchStartY - touchEndY;

      // Only handle horizontal swipes if they're more significant than vertical ones
      if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > swipeThreshold) {
        if (diffX > 0) {
          // Swipe left - next slide
          this.nextSlide();
        } else {
          // Swipe right - previous slide
          this.previousSlide();
        }
      }
    };

    this.handleSwipe = handleSwipe;

    // Prevent context menu on long touch
    document.addEventListener('contextmenu', (e) => {
      e.preventDefault();
    });

    // Mouse wheel support
    document.addEventListener('wheel', (e) => {
      if (Math.abs(e.deltaY) > 50) { // Threshold to prevent accidental scrolling
        if (e.deltaY > 0) {
          this.nextSlide();
        } else {
          this.previousSlide();
        }
        e.preventDefault();
      }
    }, { passive: false });
  }

  updateSlideDisplay() {
    const slides = document.querySelectorAll('.slide');

    slides.forEach((slide, index) => {
      const slideNumber = index + 1;
      slide.classList.remove('active', 'prev');

      if (slideNumber === this.currentSlide) {
        slide.classList.add('active');
      } else if (slideNumber < this.currentSlide) {
        slide.classList.add('prev');
      }
    });
  }

  updateNavigationButtons() {
    if (this.prevBtn) {
      this.prevBtn.disabled = this.currentSlide === 1;
    }

    if (this.nextBtn) {
      this.nextBtn.disabled = this.currentSlide === this.totalSlides;
    }
  }

  updateProgressBar() {
    if (this.progressFill) {
      const progress = (this.currentSlide / this.totalSlides) * 100;
      this.progressFill.style.width = `${progress}%`;
    }
  }

  updateSlideCounter() {
    if (this.slideCounter) {
      this.slideCounter.textContent = `Slide ${this.currentSlide} de ${this.totalSlides}`;
    }
  }

  nextSlide() {
    if (this.currentSlide < this.totalSlides) {
      this.currentSlide++;
      this.updateSlideDisplay();
      this.updateNavigationButtons();
      this.updateProgressBar();
      this.updateSlideCounter();
      console.log(`Navegou para slide ${this.currentSlide}`);
    }
  }

  previousSlide() {
    if (this.currentSlide > 1) {
      this.currentSlide--;
      this.updateSlideDisplay();
      this.updateNavigationButtons();
      this.updateProgressBar();
      this.updateSlideCounter();
      console.log(`Navegou para slide ${this.currentSlide}`);
    }
  }

  goToSlide(slideNumber) {
    if (slideNumber >= 1 && slideNumber <= this.totalSlides && slideNumber !== this.currentSlide) {
      this.currentSlide = slideNumber;
      this.updateSlideDisplay();
      this.updateNavigationButtons();
      this.updateProgressBar();
      this.updateSlideCounter();
      console.log(`Navegou diretamente para slide ${this.currentSlide}`);
    }
  }

  // Public methods for external control
  getCurrentSlide() {
    return this.currentSlide;
  }

  getTotalSlides() {
    return this.totalSlides;
  }

  // Fullscreen support
  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.log(`Error attempting to enable fullscreen: ${err.message}`);
      });
    } else {
      document.exitFullscreen();
    }
  }
}

// Global variable to access presentation
let presentation;

// Initialize when DOM is fully loaded
function initPresentation() {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      presentation = new SlidePresentation();
    });
  } else {
    presentation = new SlidePresentation();
  }
}

// Initialize presentation
initPresentation();

// Global functions for debugging and external control
window.goToSlide = function(slideNumber) {
  if (presentation) {
    presentation.goToSlide(slideNumber);
  }
};

window.nextSlide = function() {
  if (presentation) {
    presentation.nextSlide();
  }
};

window.previousSlide = function() {
  if (presentation) {
    presentation.previousSlide();
  }
};

window.getCurrentSlide = function() {
  return presentation ? presentation.getCurrentSlide() : 1;
};

window.toggleFullscreen = function() {
  if (presentation) {
    presentation.toggleFullscreen();
  }
};

// Handle visibility change (when tab becomes active/inactive)
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && presentation) {
    // Refresh display when tab becomes active
    presentation.updateSlideDisplay();
  }
});

// Handle window resize
window.addEventListener('resize', () => {
  if (presentation) {
    // Small delay to ensure layout has updated
    setTimeout(() => {
      presentation.updateSlideDisplay();
    }, 100);
  }
});

// Error handling
window.addEventListener('error', (e) => {
  console.error('Erro na apresentação:', e.error);
});

// Success message
console.log('Script de apresentação carregado com sucesso!');
console.log('Comandos disponíveis:');
console.log('- goToSlide(n): Ir para slide n');
console.log('- nextSlide(): Próximo slide');
console.log('- previousSlide(): Slide anterior');
console.log('- getCurrentSlide(): Slide atual');
console.log('- toggleFullscreen(): Alternar tela cheia');