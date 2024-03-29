// THIS IS AN AUTOMATICALLY GENERATED FILE.
// DO NOT MODIFY BY HAND!!
//
// Generated by zcm-gen

#include <string.h>
#ifndef ZCM_EMBEDDED
#include <stdio.h>
#endif
#include "sensor_info_t.h"

static int __sensor_info_t_hash_computed = 0;
static uint64_t __sensor_info_t_hash;

uint64_t __sensor_info_t_hash_recursive(const __zcm_hash_ptr* p)
{
    const __zcm_hash_ptr* fp;
    for (fp = p; fp != NULL; fp = fp->parent)
        if (fp->v == __sensor_info_t_get_hash)
            return 0;

    __zcm_hash_ptr cp;
    cp.parent =  p;
    cp.v = (void*)__sensor_info_t_get_hash;
    (void) cp;

    uint64_t hash = (uint64_t)0xf14ccf262fcfcc10LL
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
        ;

    return (hash<<1) + ((hash>>63)&1);
}

int64_t __sensor_info_t_get_hash(void)
{
    if (!__sensor_info_t_hash_computed) {
        __sensor_info_t_hash = (int64_t)__sensor_info_t_hash_recursive(NULL);
        __sensor_info_t_hash_computed = 1;
    }

    return __sensor_info_t_hash;
}

int __sensor_info_t_encode_array(void* buf, uint32_t offset, uint32_t maxlen, const sensor_info_t* p, uint32_t elements)
{
    uint32_t pos_byte = 0, element;
    int thislen;

    for (element = 0; element < elements; ++element) {

        /* imu_acceleration_x */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_x), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_acceleration_y */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_y), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_acceleration_z */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_z), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_gyroscope */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_gyroscope), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_magnetometer */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_magnetometer), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* pressure */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].pressure), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* temperature */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].temperature), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* proximity */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].proximity), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* distance */
        thislen = __float_encode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].distance), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

    }
    return pos_byte;
}

int sensor_info_t_encode(void* buf, uint32_t offset, uint32_t maxlen, const sensor_info_t* p)
{
    uint32_t pos = 0;
    int thislen;
    int64_t hash = __sensor_info_t_get_hash();

    thislen = __int64_t_encode_array(buf, offset + pos, maxlen - pos, &hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    thislen = __sensor_info_t_encode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

uint32_t __sensor_info_t_encoded_array_size(const sensor_info_t* p, uint32_t elements)
{
    uint32_t size = 0, element;
    for (element = 0; element < elements; ++element) {

        size += __float_encoded_array_size(&(p[element].imu_acceleration_x), 1); // imu_acceleration_x

        size += __float_encoded_array_size(&(p[element].imu_acceleration_y), 1); // imu_acceleration_y

        size += __float_encoded_array_size(&(p[element].imu_acceleration_z), 1); // imu_acceleration_z

        size += __float_encoded_array_size(&(p[element].imu_gyroscope), 1); // imu_gyroscope

        size += __float_encoded_array_size(&(p[element].imu_magnetometer), 1); // imu_magnetometer

        size += __float_encoded_array_size(&(p[element].pressure), 1); // pressure

        size += __float_encoded_array_size(&(p[element].temperature), 1); // temperature

        size += __float_encoded_array_size(&(p[element].proximity), 1); // proximity

        size += __float_encoded_array_size(&(p[element].distance), 1); // distance

    }
    return size;
}

uint32_t sensor_info_t_encoded_size(const sensor_info_t* p)
{
    return 8 + __sensor_info_t_encoded_array_size(p, 1);
}

int __sensor_info_t_decode_array(const void* buf, uint32_t offset, uint32_t maxlen, sensor_info_t* p, uint32_t elements)
{
    uint32_t pos_byte = 0, element;
    int thislen;

    for (element = 0; element < elements; ++element) {

        /* imu_acceleration_x */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_x), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_acceleration_y */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_y), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_acceleration_z */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_acceleration_z), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_gyroscope */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_gyroscope), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* imu_magnetometer */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].imu_magnetometer), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* pressure */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].pressure), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* temperature */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].temperature), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* proximity */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].proximity), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

        /* distance */
        thislen = __float_decode_array(buf, offset + pos_byte, maxlen - pos_byte, &(p[element].distance), 1);
        if (thislen < 0) return thislen; else pos_byte += thislen;

    }
    return pos_byte;
}

int __sensor_info_t_decode_array_cleanup(sensor_info_t* p, uint32_t elements)
{
    uint32_t element;
    for (element = 0; element < elements; ++element) {

        __float_decode_array_cleanup(&(p[element].imu_acceleration_x), 1);

        __float_decode_array_cleanup(&(p[element].imu_acceleration_y), 1);

        __float_decode_array_cleanup(&(p[element].imu_acceleration_z), 1);

        __float_decode_array_cleanup(&(p[element].imu_gyroscope), 1);

        __float_decode_array_cleanup(&(p[element].imu_magnetometer), 1);

        __float_decode_array_cleanup(&(p[element].pressure), 1);

        __float_decode_array_cleanup(&(p[element].temperature), 1);

        __float_decode_array_cleanup(&(p[element].proximity), 1);

        __float_decode_array_cleanup(&(p[element].distance), 1);

    }
    return 0;
}

int sensor_info_t_decode(const void* buf, uint32_t offset, uint32_t maxlen, sensor_info_t* p)
{
    uint32_t pos = 0;
    int thislen;
    int64_t hash = __sensor_info_t_get_hash();

    int64_t this_hash;
    thislen = __int64_t_decode_array(buf, offset + pos, maxlen - pos, &this_hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;
    if (this_hash != hash) return -1;

    thislen = __sensor_info_t_decode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

int sensor_info_t_decode_cleanup(sensor_info_t* p)
{
    return __sensor_info_t_decode_array_cleanup(p, 1);
}

uint32_t __sensor_info_t_clone_array(const sensor_info_t* p, sensor_info_t* q, uint32_t elements)
{
    uint32_t n = 0, element;
    for (element = 0; element < elements; ++element) {

        n += __float_clone_array(&(p[element].imu_acceleration_x), &(q[element].imu_acceleration_x), 1);

        n += __float_clone_array(&(p[element].imu_acceleration_y), &(q[element].imu_acceleration_y), 1);

        n += __float_clone_array(&(p[element].imu_acceleration_z), &(q[element].imu_acceleration_z), 1);

        n += __float_clone_array(&(p[element].imu_gyroscope), &(q[element].imu_gyroscope), 1);

        n += __float_clone_array(&(p[element].imu_magnetometer), &(q[element].imu_magnetometer), 1);

        n += __float_clone_array(&(p[element].pressure), &(q[element].pressure), 1);

        n += __float_clone_array(&(p[element].temperature), &(q[element].temperature), 1);

        n += __float_clone_array(&(p[element].proximity), &(q[element].proximity), 1);

        n += __float_clone_array(&(p[element].distance), &(q[element].distance), 1);

    }
    return n;
}

sensor_info_t* sensor_info_t_copy(const sensor_info_t* p)
{
    sensor_info_t* q = (sensor_info_t*) malloc(sizeof(sensor_info_t));
    __sensor_info_t_clone_array(p, q, 1);
    return q;
}

void sensor_info_t_destroy(sensor_info_t* p)
{
    __sensor_info_t_decode_array_cleanup(p, 1);
    free(p);
}

int sensor_info_t_publish(zcm_t* zcm, const char* channel, const sensor_info_t* p)
{
      uint32_t max_data_size = sensor_info_t_encoded_size (p);
      uint8_t* buf = (uint8_t*) malloc (max_data_size);
      if (!buf) return -1;
      int data_size = sensor_info_t_encode (buf, 0, max_data_size, p);
      if (data_size < 0) {
          free (buf);
          return data_size;
      }
      int status = zcm_publish (zcm, channel, buf, (uint32_t)data_size);
      free (buf);
      return status;
}

struct _sensor_info_t_subscription_t {
    sensor_info_t_handler_t user_handler;
    void* userdata;
    zcm_sub_t* z_sub;
};
static
void sensor_info_t_handler_stub (const zcm_recv_buf_t* rbuf,
                            const char* channel, void* userdata)
{
    int status;
    sensor_info_t p;
    memset(&p, 0, sizeof(sensor_info_t));
    status = sensor_info_t_decode (rbuf->data, 0, rbuf->data_size, &p);
    if (status < 0) {
        #ifndef ZCM_EMBEDDED
        fprintf (stderr, "error %d decoding sensor_info_t!!!\n", status);
        #endif
        return;
    }

    sensor_info_t_subscription_t* h = (sensor_info_t_subscription_t*) userdata;
    h->user_handler (rbuf, channel, &p, h->userdata);

    sensor_info_t_decode_cleanup (&p);
}

sensor_info_t_subscription_t* sensor_info_t_subscribe (zcm_t* zcm,
                    const char* channel,
                    sensor_info_t_handler_t f, void* userdata)
{
    sensor_info_t_subscription_t* n = (sensor_info_t_subscription_t*)
                       malloc(sizeof(sensor_info_t_subscription_t));
    n->user_handler = f;
    n->userdata = userdata;
    n->z_sub = zcm_subscribe (zcm, channel,
                              sensor_info_t_handler_stub, n);
    if (n->z_sub == NULL) {
        #ifndef ZCM_EMBEDDED
        fprintf (stderr,"couldn't reg sensor_info_t ZCM handler!\n");
        #endif
        free (n);
        return NULL;
    }
    return n;
}

int sensor_info_t_unsubscribe(zcm_t* zcm, sensor_info_t_subscription_t* hid)
{
    int status = zcm_unsubscribe (zcm, hid->z_sub);
    if (0 != status) {
        #ifndef ZCM_EMBEDDED
        fprintf(stderr,
           "couldn't unsubscribe sensor_info_t_handler %p!\n", hid);
        #endif
        return -1;
    }
    free (hid);
    return 0;
}

