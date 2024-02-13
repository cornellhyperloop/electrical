cmake_minimum_required(VERSION 3.14)
set( CMAKE_CXX_COMPILER "C:/msys64/mingw64/bin/g++.exe" ) # Path to your g++ compiler
set( CMAKE_C_COMPILER "C:/msys64/mingw64/bin/gcc.exe" ) # Path to your gcc compiler

project(state_machine)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
 
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
 
enable_testing()
 
add_executable(
  test_StateMachine
  test_StateMachine.cpp
)
target_link_libraries(
  test_StateMachine
  GTest::gtest_main
)
 
include(GoogleTest)
gtest_discover_tests(test_StateMachine)