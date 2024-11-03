
set(PROJ "conan_explorer_deploy")

add_executable(${PROJ}
    main.cpp
)
target_link_libraries(${PROJ}
    ftxui::ftxui
)

install(TARGETS ${PROJ})