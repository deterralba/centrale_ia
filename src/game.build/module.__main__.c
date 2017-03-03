/* Generated code for Python source for module '__main__'
 * created by Nuitka version 0.5.25
 *
 * This code is in part copyright 2017 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The _module___main__ is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The module constants used, if any. */
static PyObject *const_str_plain_start_time;
static PyObject *const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple;
static PyObject *const_str_plain_get_next_move;
static PyObject *const_str_plain_play;
static PyObject *const_str_plain_grid;
static PyObject *const_str_plain_ThreadMMPlayer;
static PyObject *const_str_digest_2b649fe84a0c732e87737fcc9482ab68;
static PyObject *const_str_plain_GUI;
static PyObject *const_str_plain_generate_play;
static PyObject *const_int_neg_1;
static PyObject *const_str_plain_args;
static PyObject *const_str_plain_SmartPlayer;
static PyObject *const_str_plain_draw;
extern PyObject *const_dict_empty;
static PyObject *const_tuple_str_plain_RandomPlayer_tuple;
static PyObject *const_str_plain_time;
static PyObject *const_str_plain_actions;
static PyObject *const_tuple_int_pos_4_int_pos_5_tuple;
extern PyObject *const_str_plain_site;
extern PyObject *const_str_plain___main__;
static PyObject *const_str_angle_module;
static PyObject *const_tuple_str_plain_x_tuple;
static PyObject *const_str_plain_do_actions;
static PyObject *const_str_plain_start_GUI;
static PyObject *const_str_plain_minmax_player;
static PyObject *const_str_plain_types;
static PyObject *const_str_plain_Board;
static PyObject *const_str_plain_os;
extern PyObject *const_str_plain___doc__;
static PyObject *const_tuple_str_plain_sleep_str_plain_time_tuple;
static PyObject *const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple;
static PyObject *const_str_digest_85b1881b8a9238c4f072391a62395c64;
extern PyObject *const_int_0;
static PyObject *const_str_plain_WOLV;
static PyObject *const_str_digest_082d0ba1ec0af33f66d14bd05b0dd354;
static PyObject *const_str_plain_VAMP;
static PyObject *const_str_plain_race;
static PyObject *const_str_plain_sleep;
static PyObject *const_tuple_str_plain_Board_tuple;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_plain_RandomPlayer;
static PyObject *const_str_plain_player1;
static PyObject *const_str_plain_player2;
extern PyObject *const_str_plain_format;
static PyObject *const_int_pos_4;
static PyObject *const_int_pos_5;
static PyObject *const_str_plain_board;
static PyObject *const_int_pos_3;
extern PyObject *const_int_pos_1;
static PyObject *const_str_digest_61f12b06f111ecec1c789994145c28ca;
static PyObject *const_str_plain_current_player;
extern PyObject *const_tuple_empty;
static PyObject *const_str_plain_HUM;
static PyObject *const_str_plain_const;
static PyObject *const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple;
static PyObject *const_str_plain_player;
static PyObject *const_dict_fb624de6487b655ee498f99cfc17752e;
static PyObject *const_tuple_str_plain_start_GUI_str_plain_draw_tuple;
static PyObject *const_str_plain_x;
static PyObject *const_str_plain_y;
static PyObject *const_str_plain_depth;
static PyObject *const_tuple_str_plain_SmartPlayer_str_plain_ThreadMMPlayer_tuple;
static PyObject *const_int_pos_2;
static PyObject *const_str_plain_initial_pop;
static PyObject *const_str_plain_is_over;
static PyObject *const_str_angle_lambda;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_start_time = UNSTREAM_STRING( &constant_bin[ 0 ], 10, 1 );
    const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple = PyTuple_New( 3 );
    const_str_plain_HUM = UNSTREAM_STRING( &constant_bin[ 10 ], 3, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple, 0, const_str_plain_HUM ); Py_INCREF( const_str_plain_HUM );
    const_str_plain_WOLV = UNSTREAM_STRING( &constant_bin[ 13 ], 4, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple, 1, const_str_plain_WOLV ); Py_INCREF( const_str_plain_WOLV );
    const_str_plain_VAMP = UNSTREAM_STRING( &constant_bin[ 17 ], 4, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple, 2, const_str_plain_VAMP ); Py_INCREF( const_str_plain_VAMP );
    const_str_plain_get_next_move = UNSTREAM_STRING( &constant_bin[ 21 ], 13, 1 );
    const_str_plain_play = UNSTREAM_STRING( &constant_bin[ 34 ], 4, 1 );
    const_str_plain_grid = UNSTREAM_STRING( &constant_bin[ 38 ], 4, 1 );
    const_str_plain_ThreadMMPlayer = UNSTREAM_STRING( &constant_bin[ 42 ], 14, 1 );
    const_str_digest_2b649fe84a0c732e87737fcc9482ab68 = UNSTREAM_STRING( &constant_bin[ 56 ], 19, 0 );
    const_str_plain_GUI = UNSTREAM_STRING( &constant_bin[ 75 ], 3, 1 );
    const_str_plain_generate_play = UNSTREAM_STRING( &constant_bin[ 78 ], 13, 1 );
    const_int_neg_1 = PyInt_FromLong( -1l );
    const_str_plain_args = UNSTREAM_STRING( &constant_bin[ 91 ], 4, 1 );
    const_str_plain_SmartPlayer = UNSTREAM_STRING( &constant_bin[ 95 ], 11, 1 );
    const_str_plain_draw = UNSTREAM_STRING( &constant_bin[ 106 ], 4, 1 );
    const_tuple_str_plain_RandomPlayer_tuple = PyTuple_New( 1 );
    const_str_plain_RandomPlayer = UNSTREAM_STRING( &constant_bin[ 110 ], 12, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_RandomPlayer_tuple, 0, const_str_plain_RandomPlayer ); Py_INCREF( const_str_plain_RandomPlayer );
    const_str_plain_time = UNSTREAM_STRING( &constant_bin[ 6 ], 4, 1 );
    const_str_plain_actions = UNSTREAM_STRING( &constant_bin[ 122 ], 7, 1 );
    const_tuple_int_pos_4_int_pos_5_tuple = PyTuple_New( 2 );
    const_int_pos_4 = PyInt_FromLong( 4l );
    PyTuple_SET_ITEM( const_tuple_int_pos_4_int_pos_5_tuple, 0, const_int_pos_4 ); Py_INCREF( const_int_pos_4 );
    const_int_pos_5 = PyInt_FromLong( 5l );
    PyTuple_SET_ITEM( const_tuple_int_pos_4_int_pos_5_tuple, 1, const_int_pos_5 ); Py_INCREF( const_int_pos_5 );
    const_str_angle_module = UNSTREAM_STRING( &constant_bin[ 129 ], 8, 0 );
    const_tuple_str_plain_x_tuple = PyTuple_New( 1 );
    const_str_plain_x = UNSTREAM_CHAR( 120, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_x_tuple, 0, const_str_plain_x ); Py_INCREF( const_str_plain_x );
    const_str_plain_do_actions = UNSTREAM_STRING( &constant_bin[ 137 ], 10, 1 );
    const_str_plain_start_GUI = UNSTREAM_STRING( &constant_bin[ 147 ], 9, 1 );
    const_str_plain_minmax_player = UNSTREAM_STRING( &constant_bin[ 156 ], 13, 1 );
    const_str_plain_types = UNSTREAM_STRING( &constant_bin[ 169 ], 5, 1 );
    const_str_plain_Board = UNSTREAM_STRING( &constant_bin[ 174 ], 5, 1 );
    const_str_plain_os = UNSTREAM_STRING( &constant_bin[ 179 ], 2, 1 );
    const_tuple_str_plain_sleep_str_plain_time_tuple = PyTuple_New( 2 );
    const_str_plain_sleep = UNSTREAM_STRING( &constant_bin[ 181 ], 5, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_sleep_str_plain_time_tuple, 0, const_str_plain_sleep ); Py_INCREF( const_str_plain_sleep );
    PyTuple_SET_ITEM( const_tuple_str_plain_sleep_str_plain_time_tuple, 1, const_str_plain_time ); Py_INCREF( const_str_plain_time );
    const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple = PyTuple_New( 5 );
    const_str_plain_player1 = UNSTREAM_STRING( &constant_bin[ 186 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 0, const_str_plain_player1 ); Py_INCREF( const_str_plain_player1 );
    const_str_plain_player2 = UNSTREAM_STRING( &constant_bin[ 193 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 1, const_str_plain_player2 ); Py_INCREF( const_str_plain_player2 );
    const_str_plain_board = UNSTREAM_STRING( &constant_bin[ 200 ], 5, 1 );
    PyTuple_SET_ITEM( const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 2, const_str_plain_board ); Py_INCREF( const_str_plain_board );
    PyTuple_SET_ITEM( const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 3, const_str_plain_draw ); Py_INCREF( const_str_plain_draw );
    PyTuple_SET_ITEM( const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 4, const_str_plain_play ); Py_INCREF( const_str_plain_play );
    const_str_digest_85b1881b8a9238c4f072391a62395c64 = UNSTREAM_STRING( &constant_bin[ 205 ], 29, 0 );
    const_str_digest_082d0ba1ec0af33f66d14bd05b0dd354 = UNSTREAM_STRING( &constant_bin[ 234 ], 61, 0 );
    const_str_plain_race = UNSTREAM_STRING( &constant_bin[ 295 ], 4, 1 );
    const_tuple_str_plain_Board_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_Board_tuple, 0, const_str_plain_Board ); Py_INCREF( const_str_plain_Board );
    const_int_pos_3 = PyInt_FromLong( 3l );
    const_str_digest_61f12b06f111ecec1c789994145c28ca = UNSTREAM_STRING( &constant_bin[ 299 ], 5, 0 );
    const_str_plain_current_player = UNSTREAM_STRING( &constant_bin[ 304 ], 14, 1 );
    const_str_plain_const = UNSTREAM_STRING( &constant_bin[ 318 ], 5, 1 );
    const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple = PyTuple_New( 8 );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 0, const_str_plain_args ); Py_INCREF( const_str_plain_args );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 1, const_str_plain_current_player ); Py_INCREF( const_str_plain_current_player );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 2, const_str_plain_start_time ); Py_INCREF( const_str_plain_start_time );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 3, const_str_plain_actions ); Py_INCREF( const_str_plain_actions );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 4, const_str_plain_player1 ); Py_INCREF( const_str_plain_player1 );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 5, const_str_plain_board ); Py_INCREF( const_str_plain_board );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 6, const_str_plain_draw ); Py_INCREF( const_str_plain_draw );
    PyTuple_SET_ITEM( const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 7, const_str_plain_player2 ); Py_INCREF( const_str_plain_player2 );
    const_str_plain_player = UNSTREAM_STRING( &constant_bin[ 163 ], 6, 1 );
    const_dict_fb624de6487b655ee498f99cfc17752e = _PyDict_NewPresized( 1 );
    const_str_plain_depth = UNSTREAM_STRING( &constant_bin[ 323 ], 5, 1 );
    PyDict_SetItem( const_dict_fb624de6487b655ee498f99cfc17752e, const_str_plain_depth, const_int_pos_5 );
    assert( PyDict_Size( const_dict_fb624de6487b655ee498f99cfc17752e ) == 1 );
    const_tuple_str_plain_start_GUI_str_plain_draw_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_start_GUI_str_plain_draw_tuple, 0, const_str_plain_start_GUI ); Py_INCREF( const_str_plain_start_GUI );
    PyTuple_SET_ITEM( const_tuple_str_plain_start_GUI_str_plain_draw_tuple, 1, const_str_plain_draw ); Py_INCREF( const_str_plain_draw );
    const_str_plain_y = UNSTREAM_CHAR( 121, 1 );
    const_tuple_str_plain_SmartPlayer_str_plain_ThreadMMPlayer_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_SmartPlayer_str_plain_ThreadMMPlayer_tuple, 0, const_str_plain_SmartPlayer ); Py_INCREF( const_str_plain_SmartPlayer );
    PyTuple_SET_ITEM( const_tuple_str_plain_SmartPlayer_str_plain_ThreadMMPlayer_tuple, 1, const_str_plain_ThreadMMPlayer ); Py_INCREF( const_str_plain_ThreadMMPlayer );
    const_int_pos_2 = PyInt_FromLong( 2l );
    const_str_plain_initial_pop = UNSTREAM_STRING( &constant_bin[ 328 ], 11, 1 );
    const_str_plain_is_over = UNSTREAM_STRING( &constant_bin[ 339 ], 7, 1 );
    const_str_angle_lambda = UNSTREAM_STRING( &constant_bin[ 346 ], 8, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_07117f3246acc53b939d614915bdd769;
static PyCodeObject *codeobj_449afe63ddd7b8f2f4c5216c856cbfd6;
static PyCodeObject *codeobj_917ec5c1aaf76d67b850e8a0e6524283;
static PyCodeObject *codeobj_2d3cbd38ba8d0cf01424fe3db1629044;
/* For use in MainProgram.cpp. */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void)
{
    module_filename_obj = const_str_digest_082d0ba1ec0af33f66d14bd05b0dd354;
    codeobj_07117f3246acc53b939d614915bdd769 = MAKE_CODEOBJ( module_filename_obj, const_str_angle_lambda, 8, const_tuple_str_plain_x_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_449afe63ddd7b8f2f4c5216c856cbfd6 = MAKE_CODEOBJ( module_filename_obj, const_str_angle_module, 1, const_tuple_empty, 0, CO_NOFREE );
    codeobj_main = codeobj_449afe63ddd7b8f2f4c5216c856cbfd6;
    codeobj_917ec5c1aaf76d67b850e8a0e6524283 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_generate_play, 8, const_tuple_de8524dae672a419f0b9a51681f4ed61_tuple, 4, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_2d3cbd38ba8d0cf01424fe3db1629044 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_play, 9, const_tuple_ba7311f01026e8753539ba576cfa25b9_tuple, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARARGS );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION___main__$$$function_1_lambda(  );


static PyObject *MAKE_FUNCTION___main__$$$function_2_generate_play( PyObject *defaults );


static PyObject *MAKE_FUNCTION___main__$$$function_2_generate_play$$$function_1_play( struct Nuitka_CellObject *closure_board, struct Nuitka_CellObject *closure_draw, struct Nuitka_CellObject *closure_player1, struct Nuitka_CellObject *closure_player2 );


// The module function definitions.
static PyObject *impl___main__$$$function_1_lambda( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_x = python_pars[ 0 ];
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__$$$function_1_lambda );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_x );
    Py_DECREF( par_x );
    par_x = NULL;

    goto function_return_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__$$$function_1_lambda );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl___main__$$$function_2_generate_play( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_CellObject *par_player1 = PyCell_NEW1( python_pars[ 0 ] );
    struct Nuitka_CellObject *par_player2 = PyCell_NEW1( python_pars[ 1 ] );
    struct Nuitka_CellObject *par_board = PyCell_NEW1( python_pars[ 2 ] );
    struct Nuitka_CellObject *par_draw = PyCell_NEW1( python_pars[ 3 ] );
    PyObject *var_play = NULL;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = MAKE_FUNCTION___main__$$$function_2_generate_play$$$function_1_play( par_board, par_draw, par_player1, par_player2 );
    assert( var_play == NULL );
    var_play = tmp_assign_source_1;

    // Tried code:
    tmp_return_value = var_play;

    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__$$$function_2_generate_play );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_player1 );
    Py_DECREF( par_player1 );
    par_player1 = NULL;

    CHECK_OBJECT( (PyObject *)par_player2 );
    Py_DECREF( par_player2 );
    par_player2 = NULL;

    CHECK_OBJECT( (PyObject *)par_board );
    Py_DECREF( par_board );
    par_board = NULL;

    CHECK_OBJECT( (PyObject *)par_draw );
    Py_DECREF( par_draw );
    par_draw = NULL;

    CHECK_OBJECT( (PyObject *)var_play );
    Py_DECREF( var_play );
    var_play = NULL;

    goto function_return_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__$$$function_2_generate_play );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl___main__$$$function_2_generate_play$$$function_1_play( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_args = python_pars[ 0 ];
    PyObject *var_current_player = NULL;
    PyObject *var_start_time = NULL;
    PyObject *var_actions = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_assattr_name_1;
    PyObject *tmp_assattr_target_1;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_called_instance_1;
    PyObject *tmp_called_instance_2;
    PyObject *tmp_called_instance_3;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    int tmp_cmp_Eq_1;
    int tmp_cmp_Gt_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    int tmp_cond_truth_1;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_left_name_1;
    PyObject *tmp_left_name_2;
    PyObject *tmp_print_value;
    bool tmp_result;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_right_name_2;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = PyCell_GET( self->m_closure[2] );

    if ( tmp_assign_source_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "player1" );
        exception_tb = NULL;


        goto function_exception_exit;
    }

    assert( var_current_player == NULL );
    Py_INCREF( tmp_assign_source_1 );
    var_current_player = tmp_assign_source_1;

    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_2d3cbd38ba8d0cf01424fe3db1629044, module___main__ );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    loop_start_1:;
    tmp_called_instance_1 = PyCell_GET( self->m_closure[0] );

    if ( tmp_called_instance_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 11;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 11;
    tmp_cond_value_1 = CALL_METHOD_NO_ARGS( tmp_called_instance_1, const_str_plain_is_over );
    if ( tmp_cond_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_cond_value_1 );

        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    goto loop_end_1;
    branch_no_1:;
    tmp_source_name_1 = var_current_player;

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "current_player" );
        exception_tb = NULL;

        exception_lineno = 12;
        goto frame_exception_exit_1;
    }

    tmp_assattr_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_race );
    if ( tmp_assattr_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    tmp_assattr_target_1 = PyCell_GET( self->m_closure[0] );

    if ( tmp_assattr_target_1 == NULL )
    {
        Py_DECREF( tmp_assattr_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 12;
        goto frame_exception_exit_1;
    }

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_1, const_str_plain_current_player, tmp_assattr_name_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assattr_name_1 );

        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_assattr_name_1 );
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_time );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_time );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "time" );
        exception_tb = NULL;

        exception_lineno = 13;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 13;
    tmp_assign_source_2 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 13;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = var_start_time;
        var_start_time = tmp_assign_source_2;
        Py_XDECREF( old );
    }

    tmp_source_name_2 = var_current_player;

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "current_player" );
        exception_tb = NULL;

        exception_lineno = 14;
        goto frame_exception_exit_1;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_get_next_move );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 14;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = PyCell_GET( self->m_closure[0] );

    if ( tmp_args_element_name_1 == NULL )
    {
        Py_DECREF( tmp_called_name_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 14;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 14;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_assign_source_3 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 14;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = var_actions;
        var_actions = tmp_assign_source_3;
        Py_XDECREF( old );
    }

    tmp_called_name_3 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_time );

    if (unlikely( tmp_called_name_3 == NULL ))
    {
        tmp_called_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_time );
    }

    if ( tmp_called_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "time" );
        exception_tb = NULL;

        exception_lineno = 15;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 15;
    tmp_left_name_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_3 );
    if ( tmp_left_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 15;
        goto frame_exception_exit_1;
    }
    tmp_right_name_1 = var_start_time;

    tmp_compare_left_1 = BINARY_OPERATION_SUB( tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_left_name_1 );
    if ( tmp_compare_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 15;
        goto frame_exception_exit_1;
    }
    tmp_compare_right_1 = const_int_pos_2;
    tmp_cmp_Gt_1 = RICH_COMPARE_BOOL_GT( tmp_compare_left_1, tmp_compare_right_1 );
    if ( tmp_cmp_Gt_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_left_1 );

        exception_lineno = 15;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_compare_left_1 );
    if ( tmp_cmp_Gt_1 == 1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_source_name_3 = const_str_digest_85b1881b8a9238c4f072391a62395c64;
    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_format );
    assert( tmp_called_name_4 != NULL );
    tmp_args_element_name_2 = var_current_player;

    if ( tmp_args_element_name_2 == NULL )
    {
        Py_DECREF( tmp_called_name_4 );
        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "current_player" );
        exception_tb = NULL;

        exception_lineno = 16;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 16;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_print_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_print_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 16;
        goto frame_exception_exit_1;
    }
    if ( PRINT_ITEM( tmp_print_value ) == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_print_value );

        exception_lineno = 16;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_print_value );
    if ( PRINT_NEW_LINE() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 16;
        goto frame_exception_exit_1;
    }
    branch_no_2:;
    tmp_source_name_4 = const_str_digest_2b649fe84a0c732e87737fcc9482ab68;
    tmp_called_name_5 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_format );
    assert( tmp_called_name_5 != NULL );
    tmp_source_name_5 = PyCell_GET( self->m_closure[0] );

    if ( tmp_source_name_5 == NULL )
    {
        Py_DECREF( tmp_called_name_5 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 18;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_current_player );
    if ( tmp_args_element_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_5 );

        exception_lineno = 18;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_4 = var_actions;

    frame_function->f_lineno = 18;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4 };
        tmp_print_value = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_5, call_args );
    }

    Py_DECREF( tmp_called_name_5 );
    Py_DECREF( tmp_args_element_name_3 );
    if ( tmp_print_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 18;
        goto frame_exception_exit_1;
    }
    if ( PRINT_ITEM( tmp_print_value ) == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_print_value );

        exception_lineno = 18;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_print_value );
    if ( PRINT_NEW_LINE() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 18;
        goto frame_exception_exit_1;
    }
    tmp_called_instance_2 = PyCell_GET( self->m_closure[0] );

    if ( tmp_called_instance_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 19;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_5 = var_actions;

    frame_function->f_lineno = 19;
    {
        PyObject *call_args[] = { tmp_args_element_name_5 };
        tmp_unused = CALL_METHOD_WITH_ARGS1( tmp_called_instance_2, const_str_plain_do_actions, call_args );
    }

    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_called_name_6 = PyCell_GET( self->m_closure[1] );

    if ( tmp_called_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "draw" );
        exception_tb = NULL;

        exception_lineno = 20;
        goto frame_exception_exit_1;
    }

    tmp_source_name_6 = PyCell_GET( self->m_closure[0] );

    if ( tmp_source_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 20;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_grid );
    if ( tmp_args_element_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 20;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 20;
    {
        PyObject *call_args[] = { tmp_args_element_name_6 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_6, call_args );
    }

    Py_DECREF( tmp_args_element_name_6 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 20;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_compare_left_2 = var_current_player;

    if ( tmp_compare_left_2 == NULL )
    {

        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "current_player" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto frame_exception_exit_1;
    }

    tmp_compare_right_2 = PyCell_GET( self->m_closure[2] );

    if ( tmp_compare_right_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "player1" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto frame_exception_exit_1;
    }

    tmp_cmp_Eq_1 = RICH_COMPARE_BOOL_EQ( tmp_compare_left_2, tmp_compare_right_2 );
    if ( tmp_cmp_Eq_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    if ( tmp_cmp_Eq_1 == 1 )
    {
        goto condexpr_true_1;
    }
    else
    {
        goto condexpr_false_1;
    }
    condexpr_true_1:;
    tmp_assign_source_4 = PyCell_GET( self->m_closure[3] );

    if ( tmp_assign_source_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "player2" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto frame_exception_exit_1;
    }

    goto condexpr_end_1;
    condexpr_false_1:;
    tmp_assign_source_4 = PyCell_GET( self->m_closure[2] );

    if ( tmp_assign_source_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "player1" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto frame_exception_exit_1;
    }

    condexpr_end_1:;
    {
        PyObject *old = var_current_player;
        var_current_player = tmp_assign_source_4;
        Py_INCREF( var_current_player );
        Py_XDECREF( old );
    }

    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    goto loop_start_1;
    loop_end_1:;
    tmp_called_instance_3 = PyCell_GET( self->m_closure[0] );

    if ( tmp_called_instance_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "free variable '%s' referenced before assignment in enclosing scope", "board" );
        exception_tb = NULL;

        exception_lineno = 24;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 24;
    tmp_left_name_2 = CALL_METHOD_NO_ARGS( tmp_called_instance_3, const_str_plain_is_over );
    if ( tmp_left_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    tmp_right_name_2 = const_str_digest_61f12b06f111ecec1c789994145c28ca;
    tmp_print_value = BINARY_OPERATION_ADD( tmp_left_name_2, tmp_right_name_2 );
    Py_DECREF( tmp_left_name_2 );
    if ( tmp_print_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    if ( PRINT_ITEM( tmp_print_value ) == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_print_value );

        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_print_value );
    if ( PRINT_NEW_LINE() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( par_args )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_args,
                    par_args
                );

                assert( res == 0 );
            }

            if ( var_current_player )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_current_player,
                    var_current_player
                );

                assert( res == 0 );
            }

            if ( var_start_time )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_start_time,
                    var_start_time
                );

                assert( res == 0 );
            }

            if ( var_actions )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_actions,
                    var_actions
                );

                assert( res == 0 );
            }

            if ( self->m_closure[2]->ob_ref )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_player1,
                    self->m_closure[2]->ob_ref
                );

                assert( res == 0 );
            }

            if ( self->m_closure[0]->ob_ref )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_board,
                    self->m_closure[0]->ob_ref
                );

                assert( res == 0 );
            }

            if ( self->m_closure[1]->ob_ref )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_draw,
                    self->m_closure[1]->ob_ref
                );

                assert( res == 0 );
            }

            if ( self->m_closure[3]->ob_ref )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_player2,
                    self->m_closure[3]->ob_ref
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__$$$function_2_generate_play$$$function_1_play );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_args );
    Py_DECREF( par_args );
    par_args = NULL;

    Py_XDECREF( var_current_player );
    var_current_player = NULL;

    Py_XDECREF( var_start_time );
    var_start_time = NULL;

    Py_XDECREF( var_actions );
    var_actions = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_args );
    Py_DECREF( par_args );
    par_args = NULL;

    Py_XDECREF( var_current_player );
    var_current_player = NULL;

    Py_XDECREF( var_start_time );
    var_start_time = NULL;

    Py_XDECREF( var_actions );
    var_actions = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__$$$function_2_generate_play$$$function_1_play );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}



static PyObject *MAKE_FUNCTION___main__$$$function_1_lambda(  )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl___main__$$$function_1_lambda,
        const_str_angle_lambda,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_07117f3246acc53b939d614915bdd769,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module___main__,
        Py_None,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION___main__$$$function_2_generate_play( PyObject *defaults )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl___main__$$$function_2_generate_play,
        const_str_plain_generate_play,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_917ec5c1aaf76d67b850e8a0e6524283,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module___main__,
        Py_None,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION___main__$$$function_2_generate_play$$$function_1_play( struct Nuitka_CellObject *closure_board, struct Nuitka_CellObject *closure_draw, struct Nuitka_CellObject *closure_player1, struct Nuitka_CellObject *closure_player2 )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl___main__$$$function_2_generate_play$$$function_1_play,
        const_str_plain_play,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_2d3cbd38ba8d0cf01424fe3db1629044,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module___main__,
        Py_None,
        4
    );

result->m_closure[0] = closure_board;
Py_INCREF( result->m_closure[0] );
result->m_closure[1] = closure_draw;
Py_INCREF( result->m_closure[1] );
result->m_closure[2] = closure_player1;
Py_INCREF( result->m_closure[2] );
result->m_closure[3] = closure_player2;
Py_INCREF( result->m_closure[3] );

    return (PyObject *)result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineType();
extern void _initCompiledCoroutineWrapperType();
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();

#if PYTHON_VERSION >= 350
    _initCompiledCoroutineType();
    _initCompiledCoroutineWrapperType();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = (PyDictObject *)((PyModuleObject *)module___main__)->md_dict;

    CHECK_OBJECT( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module___main__ );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *tmp_import_from_1__module = NULL;
    PyObject *tmp_import_from_2__module = NULL;
    PyObject *tmp_import_from_3__module = NULL;
    PyObject *tmp_import_from_4__module = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;
    PyObject *exception_keeper_type_4;
    PyObject *exception_keeper_value_4;
    PyTracebackObject *exception_keeper_tb_4;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_4;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_args_element_name_7;
    PyObject *tmp_args_element_name_8;
    PyObject *tmp_args_element_name_9;
    PyObject *tmp_args_element_name_10;
    PyObject *tmp_args_element_name_11;
    PyObject *tmp_args_name_1;
    PyObject *tmp_args_name_2;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_assign_source_10;
    PyObject *tmp_assign_source_11;
    PyObject *tmp_assign_source_12;
    PyObject *tmp_assign_source_13;
    PyObject *tmp_assign_source_14;
    PyObject *tmp_assign_source_15;
    PyObject *tmp_assign_source_16;
    PyObject *tmp_assign_source_17;
    PyObject *tmp_assign_source_18;
    PyObject *tmp_assign_source_19;
    PyObject *tmp_assign_source_20;
    PyObject *tmp_assign_source_21;
    PyObject *tmp_assign_source_22;
    PyObject *tmp_assign_source_23;
    PyObject *tmp_assign_source_24;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    PyObject *tmp_called_name_7;
    int tmp_cond_truth_1;
    int tmp_cond_truth_2;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_cond_value_2;
    PyObject *tmp_defaults_1;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_key_2;
    PyObject *tmp_dict_key_3;
    PyObject *tmp_dict_key_4;
    PyObject *tmp_dict_key_5;
    PyObject *tmp_dict_key_6;
    PyObject *tmp_dict_key_7;
    PyObject *tmp_dict_key_8;
    PyObject *tmp_dict_key_9;
    PyObject *tmp_dict_key_10;
    PyObject *tmp_dict_key_11;
    PyObject *tmp_dict_key_12;
    PyObject *tmp_dict_key_13;
    PyObject *tmp_dict_key_14;
    PyObject *tmp_dict_key_15;
    PyObject *tmp_dict_key_16;
    PyObject *tmp_dict_key_17;
    PyObject *tmp_dict_key_18;
    PyObject *tmp_dict_key_19;
    PyObject *tmp_dict_key_20;
    PyObject *tmp_dict_key_21;
    PyObject *tmp_dict_key_22;
    PyObject *tmp_dict_key_23;
    PyObject *tmp_dict_key_24;
    PyObject *tmp_dict_key_25;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dict_value_2;
    PyObject *tmp_dict_value_3;
    PyObject *tmp_dict_value_4;
    PyObject *tmp_dict_value_5;
    PyObject *tmp_dict_value_6;
    PyObject *tmp_dict_value_7;
    PyObject *tmp_dict_value_8;
    PyObject *tmp_dict_value_9;
    PyObject *tmp_dict_value_10;
    PyObject *tmp_dict_value_11;
    PyObject *tmp_dict_value_12;
    PyObject *tmp_dict_value_13;
    PyObject *tmp_dict_value_14;
    PyObject *tmp_dict_value_15;
    PyObject *tmp_dict_value_16;
    PyObject *tmp_dict_value_17;
    PyObject *tmp_dict_value_18;
    PyObject *tmp_dict_value_19;
    PyObject *tmp_dict_value_20;
    PyObject *tmp_dict_value_21;
    PyObject *tmp_dict_value_22;
    PyObject *tmp_dict_value_23;
    PyObject *tmp_dict_value_24;
    PyObject *tmp_dict_value_25;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_import_globals_5;
    PyObject *tmp_import_globals_6;
    PyObject *tmp_import_globals_7;
    PyObject *tmp_import_globals_8;
    PyObject *tmp_import_globals_9;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyObject *tmp_import_name_from_4;
    PyObject *tmp_import_name_from_5;
    PyObject *tmp_import_name_from_6;
    PyObject *tmp_import_name_from_7;
    PyObject *tmp_import_name_from_8;
    PyObject *tmp_import_name_from_9;
    PyObject *tmp_import_name_from_10;
    PyObject *tmp_import_name_from_11;
    PyObject *tmp_kw_name_1;
    PyObject *tmp_kw_name_2;
    PyObject *tmp_list_element_1;
    int tmp_res;
    PyObject *tmp_source_name_1;
    PyObject *tmp_tuple_element_1;
    PyObject *tmp_tuple_element_2;
    PyObject *tmp_tuple_element_3;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    PyFrameObject *frame_module;


    // Module code.
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_449afe63ddd7b8f2f4c5216c856cbfd6, module___main__ );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 1;
    tmp_unused = IMPORT_MODULE( const_str_plain_os, tmp_import_globals_1, Py_None, const_tuple_empty, const_int_neg_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_import_globals_2 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 1;
    tmp_unused = IMPORT_MODULE( const_str_plain_types, tmp_import_globals_2, Py_None, const_tuple_empty, const_int_neg_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_import_globals_3 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 1;
    tmp_unused = IMPORT_MODULE( const_str_plain_site, tmp_import_globals_3, Py_None, const_tuple_empty, const_int_neg_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_082d0ba1ec0af33f66d14bd05b0dd354;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_import_globals_4 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 1;
    tmp_assign_source_3 = IMPORT_MODULE( const_str_plain_time, tmp_import_globals_4, Py_None, const_tuple_str_plain_sleep_str_plain_time_tuple, const_int_neg_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto frame_exception_exit_1;
    }
    assert( tmp_import_from_1__module == NULL );
    tmp_import_from_1__module = tmp_assign_source_3;

    // Tried code:
    tmp_import_name_from_1 = tmp_import_from_1__module;

    tmp_assign_source_4 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_sleep );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_sleep, tmp_assign_source_4 );
    tmp_import_name_from_2 = tmp_import_from_1__module;

    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_time );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_time, tmp_assign_source_5 );
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)tmp_import_from_1__module );
    Py_DECREF( tmp_import_from_1__module );
    tmp_import_from_1__module = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    CHECK_OBJECT( (PyObject *)tmp_import_from_1__module );
    Py_DECREF( tmp_import_from_1__module );
    tmp_import_from_1__module = NULL;

    tmp_import_globals_5 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 2;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain_player, tmp_import_globals_5, Py_None, const_tuple_str_plain_RandomPlayer_tuple, const_int_neg_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_RandomPlayer );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_RandomPlayer, tmp_assign_source_6 );
    tmp_import_globals_6 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 3;
    tmp_assign_source_7 = IMPORT_MODULE( const_str_plain_minmax_player, tmp_import_globals_6, Py_None, const_tuple_str_plain_SmartPlayer_str_plain_ThreadMMPlayer_tuple, const_int_neg_1 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto frame_exception_exit_1;
    }
    assert( tmp_import_from_2__module == NULL );
    tmp_import_from_2__module = tmp_assign_source_7;

    // Tried code:
    tmp_import_name_from_4 = tmp_import_from_2__module;

    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_SmartPlayer );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto try_except_handler_2;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_SmartPlayer, tmp_assign_source_8 );
    tmp_import_name_from_5 = tmp_import_from_2__module;

    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_ThreadMMPlayer );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto try_except_handler_2;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_ThreadMMPlayer, tmp_assign_source_9 );
    goto try_end_2;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)tmp_import_from_2__module );
    Py_DECREF( tmp_import_from_2__module );
    tmp_import_from_2__module = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto frame_exception_exit_1;
    // End of try:
    try_end_2:;
    CHECK_OBJECT( (PyObject *)tmp_import_from_2__module );
    Py_DECREF( tmp_import_from_2__module );
    tmp_import_from_2__module = NULL;

    tmp_import_globals_7 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 4;
    tmp_assign_source_10 = IMPORT_MODULE( const_str_plain_const, tmp_import_globals_7, Py_None, const_tuple_str_plain_HUM_str_plain_WOLV_str_plain_VAMP_tuple, const_int_neg_1 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    assert( tmp_import_from_3__module == NULL );
    tmp_import_from_3__module = tmp_assign_source_10;

    // Tried code:
    tmp_import_name_from_6 = tmp_import_from_3__module;

    tmp_assign_source_11 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_HUM );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto try_except_handler_3;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM, tmp_assign_source_11 );
    tmp_import_name_from_7 = tmp_import_from_3__module;

    tmp_assign_source_12 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_WOLV );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto try_except_handler_3;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV, tmp_assign_source_12 );
    tmp_import_name_from_8 = tmp_import_from_3__module;

    tmp_assign_source_13 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_VAMP );
    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto try_except_handler_3;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP, tmp_assign_source_13 );
    goto try_end_3;
    // Exception handler code:
    try_except_handler_3:;
    exception_keeper_type_3 = exception_type;
    exception_keeper_value_3 = exception_value;
    exception_keeper_tb_3 = exception_tb;
    exception_keeper_lineno_3 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)tmp_import_from_3__module );
    Py_DECREF( tmp_import_from_3__module );
    tmp_import_from_3__module = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_3;
    exception_value = exception_keeper_value_3;
    exception_tb = exception_keeper_tb_3;
    exception_lineno = exception_keeper_lineno_3;

    goto frame_exception_exit_1;
    // End of try:
    try_end_3:;
    CHECK_OBJECT( (PyObject *)tmp_import_from_3__module );
    Py_DECREF( tmp_import_from_3__module );
    tmp_import_from_3__module = NULL;

    tmp_import_globals_8 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 5;
    tmp_import_name_from_9 = IMPORT_MODULE( const_str_plain_board, tmp_import_globals_8, Py_None, const_tuple_str_plain_Board_tuple, const_int_neg_1 );
    if ( tmp_import_name_from_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 5;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_14 = IMPORT_NAME( tmp_import_name_from_9, const_str_plain_Board );
    Py_DECREF( tmp_import_name_from_9 );
    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 5;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_Board, tmp_assign_source_14 );
    tmp_defaults_1 = PyTuple_New( 1 );
    tmp_tuple_element_1 = MAKE_FUNCTION___main__$$$function_1_lambda(  );
    PyTuple_SET_ITEM( tmp_defaults_1, 0, tmp_tuple_element_1 );
    tmp_assign_source_15 = MAKE_FUNCTION___main__$$$function_2_generate_play( tmp_defaults_1 );
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_generate_play, tmp_assign_source_15 );
    tmp_assign_source_16 = Py_False;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain_GUI, tmp_assign_source_16 );
    tmp_cond_value_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_GUI );

    if (unlikely( tmp_cond_value_1 == NULL ))
    {
        tmp_cond_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_GUI );
    }

    if ( tmp_cond_value_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "GUI" );
        exception_tb = NULL;

        exception_lineno = 30;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_import_globals_9 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 31;
    tmp_assign_source_17 = IMPORT_MODULE( const_str_plain_draw, tmp_import_globals_9, Py_None, const_tuple_str_plain_start_GUI_str_plain_draw_tuple, const_int_neg_1 );
    if ( tmp_assign_source_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    assert( tmp_import_from_4__module == NULL );
    tmp_import_from_4__module = tmp_assign_source_17;

    // Tried code:
    tmp_import_name_from_10 = tmp_import_from_4__module;

    tmp_assign_source_18 = IMPORT_NAME( tmp_import_name_from_10, const_str_plain_start_GUI );
    if ( tmp_assign_source_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto try_except_handler_4;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_start_GUI, tmp_assign_source_18 );
    tmp_import_name_from_11 = tmp_import_from_4__module;

    tmp_assign_source_19 = IMPORT_NAME( tmp_import_name_from_11, const_str_plain_draw );
    if ( tmp_assign_source_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto try_except_handler_4;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_draw, tmp_assign_source_19 );
    goto try_end_4;
    // Exception handler code:
    try_except_handler_4:;
    exception_keeper_type_4 = exception_type;
    exception_keeper_value_4 = exception_value;
    exception_keeper_tb_4 = exception_tb;
    exception_keeper_lineno_4 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)tmp_import_from_4__module );
    Py_DECREF( tmp_import_from_4__module );
    tmp_import_from_4__module = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_4;
    exception_value = exception_keeper_value_4;
    exception_tb = exception_keeper_tb_4;
    exception_lineno = exception_keeper_lineno_4;

    goto frame_exception_exit_1;
    // End of try:
    try_end_4:;
    CHECK_OBJECT( (PyObject *)tmp_import_from_4__module );
    Py_DECREF( tmp_import_from_4__module );
    tmp_import_from_4__module = NULL;

    branch_no_1:;
    tmp_assign_source_20 = PyList_New( 5 );
    tmp_list_element_1 = _PyDict_NewPresized( 5 );
    tmp_dict_value_1 = const_int_0;
    tmp_dict_key_1 = const_str_plain_x;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_dict_value_2 = const_int_0;
    tmp_dict_key_2 = const_str_plain_y;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_2, tmp_dict_value_2 );
    tmp_dict_value_3 = const_int_0;
    tmp_dict_key_3 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM );

    if (unlikely( tmp_dict_key_3 == NULL ))
    {
        tmp_dict_key_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_HUM );
    }

    if ( tmp_dict_key_3 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "HUM" );
        exception_tb = NULL;

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_3, tmp_dict_value_3 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_4 = const_int_pos_4;
    tmp_dict_key_4 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_dict_key_4 == NULL ))
    {
        tmp_dict_key_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_dict_key_4 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_4, tmp_dict_value_4 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_5 = const_int_0;
    tmp_dict_key_5 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_dict_key_5 == NULL ))
    {
        tmp_dict_key_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_dict_key_5 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_5, tmp_dict_value_5 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 33;
        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_20, 0, tmp_list_element_1 );
    tmp_list_element_1 = _PyDict_NewPresized( 5 );
    tmp_dict_value_6 = const_int_pos_1;
    tmp_dict_key_6 = const_str_plain_x;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_6, tmp_dict_value_6 );
    tmp_dict_value_7 = const_int_pos_3;
    tmp_dict_key_7 = const_str_plain_y;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_7, tmp_dict_value_7 );
    tmp_dict_value_8 = const_int_pos_5;
    tmp_dict_key_8 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM );

    if (unlikely( tmp_dict_key_8 == NULL ))
    {
        tmp_dict_key_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_HUM );
    }

    if ( tmp_dict_key_8 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "HUM" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_8, tmp_dict_value_8 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_9 = const_int_0;
    tmp_dict_key_9 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_dict_key_9 == NULL ))
    {
        tmp_dict_key_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_dict_key_9 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_9, tmp_dict_value_9 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_10 = const_int_0;
    tmp_dict_key_10 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_dict_key_10 == NULL ))
    {
        tmp_dict_key_10 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_dict_key_10 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_10, tmp_dict_value_10 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_20, 1, tmp_list_element_1 );
    tmp_list_element_1 = _PyDict_NewPresized( 5 );
    tmp_dict_value_11 = const_int_pos_3;
    tmp_dict_key_11 = const_str_plain_x;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_11, tmp_dict_value_11 );
    tmp_dict_value_12 = const_int_pos_3;
    tmp_dict_key_12 = const_str_plain_y;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_12, tmp_dict_value_12 );
    tmp_dict_value_13 = const_int_0;
    tmp_dict_key_13 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM );

    if (unlikely( tmp_dict_key_13 == NULL ))
    {
        tmp_dict_key_13 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_HUM );
    }

    if ( tmp_dict_key_13 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "HUM" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_13, tmp_dict_value_13 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_14 = const_int_0;
    tmp_dict_key_14 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_dict_key_14 == NULL ))
    {
        tmp_dict_key_14 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_dict_key_14 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_14, tmp_dict_value_14 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_15 = const_int_pos_1;
    tmp_dict_key_15 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_dict_key_15 == NULL ))
    {
        tmp_dict_key_15 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_dict_key_15 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_15, tmp_dict_value_15 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_20, 2, tmp_list_element_1 );
    tmp_list_element_1 = _PyDict_NewPresized( 5 );
    tmp_dict_value_16 = const_int_pos_3;
    tmp_dict_key_16 = const_str_plain_x;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_16, tmp_dict_value_16 );
    tmp_dict_value_17 = const_int_pos_1;
    tmp_dict_key_17 = const_str_plain_y;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_17, tmp_dict_value_17 );
    tmp_dict_value_18 = const_int_pos_3;
    tmp_dict_key_18 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM );

    if (unlikely( tmp_dict_key_18 == NULL ))
    {
        tmp_dict_key_18 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_HUM );
    }

    if ( tmp_dict_key_18 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "HUM" );
        exception_tb = NULL;

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_18, tmp_dict_value_18 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_19 = const_int_0;
    tmp_dict_key_19 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_dict_key_19 == NULL ))
    {
        tmp_dict_key_19 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_dict_key_19 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_19, tmp_dict_value_19 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_20 = const_int_0;
    tmp_dict_key_20 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_dict_key_20 == NULL ))
    {
        tmp_dict_key_20 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_dict_key_20 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_20, tmp_dict_value_20 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_20, 3, tmp_list_element_1 );
    tmp_list_element_1 = _PyDict_NewPresized( 5 );
    tmp_dict_value_21 = const_int_pos_4;
    tmp_dict_key_21 = const_str_plain_x;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_21, tmp_dict_value_21 );
    tmp_dict_value_22 = const_int_pos_3;
    tmp_dict_key_22 = const_str_plain_y;
    PyDict_SetItem( tmp_list_element_1, tmp_dict_key_22, tmp_dict_value_22 );
    tmp_dict_value_23 = const_int_0;
    tmp_dict_key_23 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_HUM );

    if (unlikely( tmp_dict_key_23 == NULL ))
    {
        tmp_dict_key_23 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_HUM );
    }

    if ( tmp_dict_key_23 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "HUM" );
        exception_tb = NULL;

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_23, tmp_dict_value_23 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_24 = const_int_0;
    tmp_dict_key_24 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_dict_key_24 == NULL ))
    {
        tmp_dict_key_24 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_dict_key_24 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_24, tmp_dict_value_24 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_25 = const_int_pos_3;
    tmp_dict_key_25 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_dict_key_25 == NULL ))
    {
        tmp_dict_key_25 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_dict_key_25 == NULL )
    {
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_SetItem( tmp_list_element_1, tmp_dict_key_25, tmp_dict_value_25 );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_20 );
        Py_DECREF( tmp_list_element_1 );

        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_20, 4, tmp_list_element_1 );
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_initial_pop, tmp_assign_source_20 );
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_Board );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_Board );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "Board" );
        exception_tb = NULL;

        exception_lineno = 39;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = const_tuple_int_pos_4_int_pos_5_tuple;
    tmp_args_element_name_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_initial_pop );

    if (unlikely( tmp_args_element_name_2 == NULL ))
    {
        tmp_args_element_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_initial_pop );
    }

    if ( tmp_args_element_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "initial_pop" );
        exception_tb = NULL;

        exception_lineno = 39;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 39;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_21 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    if ( tmp_assign_source_21 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 39;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_board, tmp_assign_source_21 );
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_ThreadMMPlayer );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_ThreadMMPlayer );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "ThreadMMPlayer" );
        exception_tb = NULL;

        exception_lineno = 40;
        goto frame_exception_exit_1;
    }

    tmp_args_name_1 = PyTuple_New( 1 );
    tmp_tuple_element_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_VAMP );

    if (unlikely( tmp_tuple_element_2 == NULL ))
    {
        tmp_tuple_element_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_VAMP );
    }

    if ( tmp_tuple_element_2 == NULL )
    {
        Py_DECREF( tmp_args_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "VAMP" );
        exception_tb = NULL;

        exception_lineno = 40;
        goto frame_exception_exit_1;
    }

    Py_INCREF( tmp_tuple_element_2 );
    PyTuple_SET_ITEM( tmp_args_name_1, 0, tmp_tuple_element_2 );
    tmp_kw_name_1 = PyDict_Copy( const_dict_fb624de6487b655ee498f99cfc17752e );
    frame_module->f_lineno = 40;
    tmp_assign_source_22 = CALL_FUNCTION( tmp_called_name_2, tmp_args_name_1, tmp_kw_name_1 );
    Py_DECREF( tmp_args_name_1 );
    Py_DECREF( tmp_kw_name_1 );
    if ( tmp_assign_source_22 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 40;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player1, tmp_assign_source_22 );
    tmp_called_name_3 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_SmartPlayer );

    if (unlikely( tmp_called_name_3 == NULL ))
    {
        tmp_called_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_SmartPlayer );
    }

    if ( tmp_called_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "SmartPlayer" );
        exception_tb = NULL;

        exception_lineno = 42;
        goto frame_exception_exit_1;
    }

    tmp_args_name_2 = PyTuple_New( 1 );
    tmp_tuple_element_3 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WOLV );

    if (unlikely( tmp_tuple_element_3 == NULL ))
    {
        tmp_tuple_element_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WOLV );
    }

    if ( tmp_tuple_element_3 == NULL )
    {
        Py_DECREF( tmp_args_name_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "WOLV" );
        exception_tb = NULL;

        exception_lineno = 42;
        goto frame_exception_exit_1;
    }

    Py_INCREF( tmp_tuple_element_3 );
    PyTuple_SET_ITEM( tmp_args_name_2, 0, tmp_tuple_element_3 );
    tmp_kw_name_2 = PyDict_Copy( const_dict_fb624de6487b655ee498f99cfc17752e );
    frame_module->f_lineno = 42;
    tmp_assign_source_23 = CALL_FUNCTION( tmp_called_name_3, tmp_args_name_2, tmp_kw_name_2 );
    Py_DECREF( tmp_args_name_2 );
    Py_DECREF( tmp_kw_name_2 );
    if ( tmp_assign_source_23 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 42;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player2, tmp_assign_source_23 );
    tmp_cond_value_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_GUI );

    if (unlikely( tmp_cond_value_2 == NULL ))
    {
        tmp_cond_value_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_GUI );
    }

    if ( tmp_cond_value_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "GUI" );
        exception_tb = NULL;

        exception_lineno = 44;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_2 = CHECK_IF_TRUE( tmp_cond_value_2 );
    if ( tmp_cond_truth_2 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 44;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_2 == 1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_called_name_4 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_start_GUI );

    if (unlikely( tmp_called_name_4 == NULL ))
    {
        tmp_called_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_start_GUI );
    }

    if ( tmp_called_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "start_GUI" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_board );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_board );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "board" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_grid );
    if ( tmp_args_element_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 45;
        goto frame_exception_exit_1;
    }
    tmp_called_name_5 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_generate_play );

    if (unlikely( tmp_called_name_5 == NULL ))
    {
        tmp_called_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_generate_play );
    }

    if ( tmp_called_name_5 == NULL )
    {
        Py_DECREF( tmp_args_element_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "generate_play" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_5 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player1 );

    if (unlikely( tmp_args_element_name_5 == NULL ))
    {
        tmp_args_element_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_player1 );
    }

    if ( tmp_args_element_name_5 == NULL )
    {
        Py_DECREF( tmp_args_element_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "player1" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_6 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player2 );

    if (unlikely( tmp_args_element_name_6 == NULL ))
    {
        tmp_args_element_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_player2 );
    }

    if ( tmp_args_element_name_6 == NULL )
    {
        Py_DECREF( tmp_args_element_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "player2" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_7 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_board );

    if (unlikely( tmp_args_element_name_7 == NULL ))
    {
        tmp_args_element_name_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_board );
    }

    if ( tmp_args_element_name_7 == NULL )
    {
        Py_DECREF( tmp_args_element_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "board" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_8 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_draw );

    if (unlikely( tmp_args_element_name_8 == NULL ))
    {
        tmp_args_element_name_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_draw );
    }

    if ( tmp_args_element_name_8 == NULL )
    {
        Py_DECREF( tmp_args_element_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "draw" );
        exception_tb = NULL;

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 45;
    {
        PyObject *call_args[] = { tmp_args_element_name_5, tmp_args_element_name_6, tmp_args_element_name_7, tmp_args_element_name_8 };
        tmp_args_element_name_4 = CALL_FUNCTION_WITH_ARGS4( tmp_called_name_5, call_args );
    }

    if ( tmp_args_element_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_element_name_3 );

        exception_lineno = 45;
        goto frame_exception_exit_1;
    }
    frame_module->f_lineno = 45;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_args_element_name_3 );
    Py_DECREF( tmp_args_element_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 45;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    goto branch_end_2;
    branch_no_2:;
    tmp_called_name_6 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_generate_play );

    if (unlikely( tmp_called_name_6 == NULL ))
    {
        tmp_called_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_generate_play );
    }

    if ( tmp_called_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "generate_play" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_9 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player1 );

    if (unlikely( tmp_args_element_name_9 == NULL ))
    {
        tmp_args_element_name_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_player1 );
    }

    if ( tmp_args_element_name_9 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "player1" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_10 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_player2 );

    if (unlikely( tmp_args_element_name_10 == NULL ))
    {
        tmp_args_element_name_10 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_player2 );
    }

    if ( tmp_args_element_name_10 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "player2" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_11 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_board );

    if (unlikely( tmp_args_element_name_11 == NULL ))
    {
        tmp_args_element_name_11 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_board );
    }

    if ( tmp_args_element_name_11 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "board" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 47;
    {
        PyObject *call_args[] = { tmp_args_element_name_9, tmp_args_element_name_10, tmp_args_element_name_11 };
        tmp_assign_source_24 = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_6, call_args );
    }

    if ( tmp_assign_source_24 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_play, tmp_assign_source_24 );
    tmp_called_name_7 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_play );

    if (unlikely( tmp_called_name_7 == NULL ))
    {
        tmp_called_name_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_play );
    }

    if ( tmp_called_name_7 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "play" );
        exception_tb = NULL;

        exception_lineno = 48;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 48;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_name_7 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 48;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    branch_end_2:;

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_module, exception_lineno );
    }
    else if ( exception_tb->tb_frame != frame_module )
    {
        PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_module, exception_lineno );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }

    // Put the previous frame back on top.
    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_module->f_executing -= 1;
#endif
    Py_DECREF( frame_module );

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    return MOD_RETURN_VALUE( module___main__ );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
