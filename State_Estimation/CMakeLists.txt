cmake_minimum_required(VERSION 3.14)
project(State_Estimation)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)


include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip

)
include_directories(
  ${PROJECT_SOURCE_DIR}/src
)
FetchContent_MakeAvailable(googletest)
enable_testing()

set(SOURCES testStateMachine testStateMachine.cpp ${PROJECT_SOURCE_DIR}/src/constants.hpp ${PROJECT_SOURCE_DIR}/src/statemachine.cpp ${PROJECT_SOURCE_DIR}/src/statemachine.hpp ${PROJECT_SOURCE_DIR}/src/helperFunctions.hpp ${PROJECT_SOURCE_DIR}/src/SerialClass.h ${PROJECT_SOURCE_DIR}/src/serialRead.cpp )

add_executable(${SOURCES})

target_link_libraries(
  testStateMachine
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(testStateMachine)