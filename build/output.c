#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int32_t allocate(uint64_t size) {
    return;
}
int32_t allocate_zeroed(uint64_t num, uint64_t size) {
    return;
}
int32_t reallocate(uint64_t size) {
    return;
}
int32_t deallocate() {
    return;
}
int32_t print(const char* s) {
    return;
}
int32_t println(const char* s) {
    return;
}
int32_t print_int(int32_t n) {
    return;
}
int32_t print_float(float f) {
    return;
}
int32_t read_line() {
    return;
}
int32_t vec_new() {
    return;
}
int32_t vec_push(* v, uint64_t elem_size, uint64_t new_len) {
    return;
}
int32_t vec_pop(* v) {
    return;
}
int32_t vec_get(* v, uint64_t idx, uint64_t elem_size) {
    return;
}
int32_t vec_free(* v) {
    return;
}
int32_t vec_reserve(* v, uint64_t elem_size, uint64_t new_cap) {
    return;
}
int32_t string_new() {
    return;
}
int32_t string_from(* c_str) {
    return;
}
int32_t string_alloc(uint64_t len) {
    return;
}
int32_t string_concat(* a, * b) {
    return;
}
int32_t string_concat_alloc(uint64_t a_len, uint64_t b_len) {
    return;
}
int32_t string_grow(* s, uint64_t new_cap) {
    return;
}
int32_t string_free(* s) {
    return;
}
int32_t string_len_eq(uint64_t a_len, uint64_t b_len) {
    return;
}
int32_t map_new(uint64_t capacity) {
    return;
}
int32_t map_insert(* m, uint64_t key, uint64_t value, uint64_t capacity) {
    return;
}
int32_t map_get(* m, uint64_t key, uint64_t capacity) {
    return;
}
int32_t map_contains(* m, uint64_t key, uint64_t capacity) {
    return;
}
int32_t map_remove(* m, uint64_t key, uint64_t capacity) {
    return;
}
int32_t map_len(* m) {
    return;
}
int32_t map_free(* m) {
    return;
}
int32_t map_grow(* m, uint64_t old_cap, uint64_t new_cap) {
    return;
}
int32_t fs_open(* path, * mode) {
    return;
}
int32_t fs_close(* fp) {
    return;
}
int32_t fs_read(* buf, uint64_t size, uint64_t count, * fp) {
    return;
}
int32_t fs_write(* buf, uint64_t size, uint64_t count, * fp) {
    return;
}
int32_t fs_seek(* fp, int32_t offset, int32_t whence) {
    return;
}
int32_t fs_tell(* fp) {
    return;
}
int32_t fs_eof(* fp) {
    return;
}
int32_t fs_error(* fp) {
    return;
}
int32_t cli_arg_count() {
    return;
}
int32_t cli_get_arg(uint64_t index) {
    return;
}
int32_t cli_has_flag(* flag) {
    return;
}
int32_t cli_get_option(* flag) {
    return;
}
int32_t main() {
    return;
}
