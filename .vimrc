""Last update: 08.09.2017 22:20
"Settings
set tabstop=4
syntax on
set number
set incsearch
set hlsearch
set termencoding=utf8
set ruler
set showcmd
""set mouse=a 
set mousehide
set autoindent
set nowrap
set shiftwidth=4
set softtabstop=4
set smartindent
set cursorline
set history=200
set wildmenu
"" New update from vim vk
set expandtab
filetype indent on
set showmatch
set foldenable
set foldlevelstart=10
"for not hihglightings
set nohlsearch
syntax enable
filetype off
:set noswapfile
set noshowmode
"""     Colorschemes  
"" in ~/.vim/colors/badwolf.vim
colorscheme badwolf
""colorscheme OceanicNext
""colorscheme rupza
""colorscheme solarized


""Close nerdtree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

""Aliases
:imap qq <Esc>
:imap йй <Esc>
":command Я w
:command W w

nnoremap j gj
nnoremap k gk
nnoremap B ^
nnoremap E $
nnoremap $ <nop>
nnoremap ^ <nop>
nnoremap gV `[v`]
nnoremap ЯЯ wq
nmap <F8> :TagbarToggle<CR>
nnoremap <silent> <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>


"autocmd vimenter * NERDTree

map <C-n> :NERDTreeToggle<CR>
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif

"Plugins
call plug#begin('~/.vim/plugged')

Plug 'shougo/echodoc.vim'
Plug 'scrooloose/nerdcommenter'
Plug 'plasticboy/vim-markdown'
"---------=== Code/project navigation ===-------------
Plug 'scrooloose/nerdtree'           " Project and file navigation
Plug 'majutsushi/tagbar'             " Class/module browser
"
""------------------=== Other ===----------------------
Plug 'bling/vim-airline'              " Lean & mean status/tabline for vim
Plug 'fisadev/FixedTaskList.vim'      " Pending tasks list
Plug 'rosenfeld/conque-term'          " Consoles as buffers
Plug 'tpope/vim-surround'     " Parentheses, brackets, quotes, XML tags, and more

"--------------=== Snippets support ===---------------
Plug 'garbas/vim-snipmate'       " Snippets manager
Plug 'MarcWeber/vim-addon-mw-utils'  " dependencies #1
Plug 'tomtom/tlib_vim'       " dependencies #2
Plug 'honza/vim-snippets'        " snippets repo
"
""---------------=== Languages support ===-------------
" --- Python ---
Plug 'klen/python-mode'            " Python mode (docs, refactor, lints,
    "highlighting, run and ipdb and more)
Plug 'davidhalter/jedi-vim'        " Jedi-vim autocomplete plugin
Plug 'mitsuhiko/vim-jinja'     " Jinja support for vim
Plug 'mitsuhiko/vim-python-combined'  " Combined Python 2/3 for Vim
Plug 'dbsr/vimpy'
Plug 'mgedmin/python-imports.vim'

call plug#end()

filetype on
filetype plugin on
filetype plugin indent on



map <F2>    :ImportName<CR>
map <C-F2>  :ImportNameHere<CR>
map <F3>    :!ctags -R --exclude=node_modules --exclude=static --exclude=staticfiles<CR>
nnoremap tn :tabnew<bar> :NERDTreeToggle <CR>
nnoremap tc :tabclose<CR>
let g:vimpy_prompt_resolve = 1
let g:vimpy_remove_unused = 1


"Vim tabs
nnoremap gt gT
nnoremap gy gt

"Nerd_commenter
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

 " Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

 " Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

 " Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'java': { 'left': '/**','right': '**/' }, 'py':{'left':'“””','right':'“”” ' } }

let NERDTreeIgnore = ['\.pyc$']
let g:pymode_indent = 0
" Allow commenting and inverting empty lines (useful when commenting a region)

 "Use TAB to complete when typing words, else inserts TABs as usual.
 ""Uses dictionary and source files to find matching words to complete.

 "See help completion for source,
 ""Note: usual completion is on <C-n> but more trouble to press all the time.
 "Never type the same word twice and maybe learn a new spellings!
 ""Use the Linux dictionary when spelling is in doubt.
 "Window users can copy the file to their machine.

let g:pymode_rope = 0
let g:pymode_rope_completion = 0
let g:pymode_rope_complete_on_dot = 0

" документация
let g:pymode_doc = 0
let g:pymode_doc_key = 'K'
" " проверка кода
""let g:pymode_lint = 1
""let g:pymode_lint_checker = "pyflakes,pep8"
""let g:pymode_lint_ignore="E501,W601,C0110"
" " провека кода после сохранения
""let g:pymode_lint_write = 1
"
" " поддержка virtualenv
"let g:pymode_virtualenv = 1
"
" " установка breakpoints
"" let g:pymode_breakpoint = 1
"" let g:pymode_breakpoint_key = '<leader>b'
"
" " подстветка синтаксиса
""let g:pymode_syntax = 1
""let g:pymode_syntax_all = 1
""let g:pymode_syntax_indent_errors = g:pymode_syntax_all
""let g:pymode_syntax_space_errors = g:pymode_syntax_all
"
" " отключить autofold по коду
let g:pymode_folding = 0

""let g:jedi#setup_py_version="python"
" " возможность запускать код
let g:pymode_run = 0

autocmd FileType python setlocal completeopt-=preview
let g:jedi#popup_select_first = 0
let g:jedi#show_call_signatures = "0"
"let g:jedi#use_tabs_not_buffers = 1

"let g:pymode_rope = 0
"let g:jedi#completions_enabled = 0

function! Tab_Or_Complete()
      if col('.')>1 && strpart( getline('.'), col('.')-2, 3 ) =~ '^\w'
            return "\<C-N>"
      else
            return "\<Tab>"
      endif
endfunction
:inoremap <Tab> <C-R>=Tab_Or_Complete()<CR>
:set dictionary="/usr/dict/words
autocmd FileType python 
set omnifunc=syntaxcomplete#Complete  
let g:echodoc_enable_at_startup = 1
let g:jedi#show_call_signatures = 2

"fun! DetectTemplate()
"      let n = 1
"        while n < line("$")
"                if getline(n) =~ '{%' || getline(n) =~ '{{'
"                          set ft=htmldjango
"                               return
 "                                   endif
  "                                      let n = n + 1
   "                                       endwhile
    "                                        set ft=html "default html
     "                                       #endfun
