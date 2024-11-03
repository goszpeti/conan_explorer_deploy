project('conan_explorer_deploy', 'cpp',
  version : '0.1',
  default_options : ['warning_level=3', 'cpp_std=c++17'])

ftxui = dependency('ftxui', version : '>=5.0.0')
# , modules: ['ftxui::ftxui'], components: ['ftxui']

executable('conan_explorer_deploy',
           'src/main.cpp',
          #  native : true,
           install : true,
           dependencies: [ftxui])
