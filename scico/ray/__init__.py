# -*- coding: utf-8 -*-
# Copyright (C) 2022 by SCICO Developers
# All rights reserved. BSD 3-clause License.
# This file is part of the SCICO package. Details of the copyright and
# user license can be found in the 'LICENSE' file distributed with the
# package.

"""Simplified interfaces to :external:doc:`ray <ray-core/package-ref>`."""


try:
    from ray import get, put
except ImportError:
    raise ImportError("Could not import ray; please install it.")
