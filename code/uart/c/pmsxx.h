/*
 * Copyright (c) 2020, RudyLo <luhuadong@163.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Change Logs:
 * Date           Author       Notes
 * 2020-09-23     luhuadong    the first version
 */

#ifndef __PMSXX_H__
#define __PMSXX_H__

/* Custom sensor control cmd types */
#define  RT_SENSOR_CTRL_PMS_STANDBY              (0x110)   /* Standby mode (no output) */
#define  RT_SENSOR_CTRL_PMS_NORMAL               (0x111)   /* Normal  mode */
#define  RT_SENSOR_CTRL_PMS_ACTIVE               (0x112)   /* Active output mode */
#define  RT_SENSOR_CTRL_PMS_PASSIVE              (0x113)   /* Passive output mode */
#define  RT_SENSOR_CTRL_PMS_DUMP                 (0x114)   /* Dump all response */

#define PMS_READ_WAIT_TIME                       (3000)

#define FRAME_LEN_MIN                            (32)
#define FRAME_LEN_MAX                            (40)

#define FRAME_START1                             (0x42)
#define FRAME_START2                             (0x4d)

typedef enum
{
    PMS_FRAME_HEAD,
    PMS_FRAME_HEAD_ACK,
    PMS_FRAME_LENGTH,
    PMS_FRAME_PAYLOAD,
    PMS_FRAME_END

} pms_frame_t;

typedef enum
{
    PMS_MODE_READ = 0,
    PMS_MODE_PASSIVE,
    PMS_MODE_ACTIVE,
    PMS_MODE_STANDBY,
    PMS_MODE_NORMAL

} pms_mode_t;

struct pms_cmd
{
    uint8_t  START1;
    uint8_t  START2;
    uint8_t  CMD;
    uint8_t  DATAH;
    uint8_t  DATAL;
    uint8_t  LRCH;
    uint8_t  LRCL;
};
typedef struct pms_cmd *pms_cmd_t;

struct pms_response
{
    uint8_t  start1;
    uint8_t  start2;
    uint16_t length;

    uint16_t PM1_0_CF1;
    uint16_t PM2_5_CF1;
    uint16_t PM10_0_CF1;
    uint16_t PM1_0_atm;
    uint16_t PM2_5_atm;
    uint16_t PM10_0_atm;
    uint16_t air_0_3um;
    uint16_t air_0_5um;
    uint16_t air_1_0um;
    uint16_t air_2_5um;
    uint16_t air_5_0um;
    uint16_t air_10_0um;

#ifdef PKG_USING_PMSXX_ENHANCED
    uint16_t hcho;
    uint16_t temp;
    uint16_t humi;
    uint16_t reserve;
#endif

    uint8_t  version;
    uint8_t  errorCode;
    uint16_t checksum;
};
typedef struct pms_response *pms_response_t;

struct pms_device
{
    int  serial;
#ifdef PKG_USING_PMSXX_UART_DMA
    rt_mailbox_t rx_mb;
#else
    rt_sem_t     rx_sem;
#endif
    rt_sem_t     tx_done;
    rt_sem_t     ack;
    rt_thread_t  rx_tid;

    struct pms_response resp;

    rt_mutex_t   lock;
    rt_uint8_t   version;
};
typedef struct pms_device *pms_device_t;


pms_device_t pms_create(const char *uart_name);
void         pms_delete(pms_device_t dev);

rt_uint16_t  pms_read(pms_device_t dev, void *buf, rt_uint16_t size, rt_int32_t time);
rt_uint16_t  pms_wait(pms_device_t dev, void *buf, rt_uint16_t size);
rt_err_t     pms_set_mode(pms_device_t dev, pms_mode_t mode);
rt_bool_t    pms_is_ready(pms_device_t dev);

void         pms_show_command(pms_cmd_t cmd);
void         pms_show_response(pms_response_t resp);
void         pms_dump(const char *buf, rt_uint16_t size);


rt_err_t rt_hw_pms_init(const char *name, struct rt_sensor_config *cfg);

#endif /* __PMSXX_H__ */
