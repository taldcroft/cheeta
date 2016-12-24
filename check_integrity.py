#!/usr/bin/env python
"""
Check integrity of Ska archive

This is normally run as a cron job.
"""

if __name__ == '__main__':
    from Ska.engarchive import check_integrity
    check_integrity.main()
