# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import (QCoreApplication, QVariant)
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterCrs,
                       QgsProcessingParameterString,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterFeatureSink,
                       QgsFeatureRequest,
                       QgsExpression,
                       QgsField,
                       QgsFeature,
                       )
from qgis import processing


class GenerateLabel(QgsProcessingAlgorithm):
    """
    Generating Label ordered by geometry area
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    FIELD_NAME = 'FIELD_NAME'
    CRS_ID = 'CRS_ID'
    ASC_DESC = 'ASC_DESC'
    LABEL_PREFIX = 'LABEL_PREFIX'
    LABEL_SUFIX = 'LABEL_SUFIX'
    NEW_POSITION = 'new_position'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return GenerateLabel()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'generatelabel'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Generate Label')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Kyle scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'kylescripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        short_help = """Este algorìtimo  gera um novo campo LABEL no seguite formato
        PREFIXO ORDEM DA FEIÇÃO SUFIXO.
        As feições são ordenadas de acordo com a area, sendo por padrão em ordem ASCENDENTE.
        o SRC de padrão para calculo da área é o 31983
        """
        return self.tr(short_help)

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have polygons only.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )
        
        # Adds an input to set the new field name
        self.addParameter(
            QgsProcessingParameterString(
                self.FIELD_NAME,
                self.tr('Field name'),
                'new_label'
            )
        )
        
        
        # Adds an input to set the label prefix
        self.addParameter(
            QgsProcessingParameterString(
                self.LABEL_PREFIX,
                self.tr('Label Prefix'),
                'A - '
            )
        )
        
        # Adds an input to set the label sufix
        self.addParameter(
            QgsProcessingParameterString(
                self.LABEL_SUFIX,
                self.tr('Label SUFIX'),
                '',
                optional=True
            )
        )
        # Adds an input to set the new field
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.ASC_DESC,
                self.tr('Ascending'),
                True
            )
        )

        
        # Adds an input to set the new field
        self.addParameter(
            QgsProcessingParameterCrs(
                self.CRS_ID,
                self.tr('Choose CRS'),
                'EPSG:31983',
            )
        )
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )
        

        # If source was not found, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSourceError method to return a standard
        # helper text for when a source cannot be evaluated
        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        sink_fields = source.fields()
        sink_fields.append(QgsField(self.NEW_POSITION, QVariant.Int))
        sink_fields.append(QgsField(parameters['FIELD_NAME'], QVariant.String))
        
        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            sink_fields,
            source.wkbType(),
            source.sourceCrs()
        )

        # Send some information to the user
        feedback.pushInfo('New field name: {}'.format(parameters['FIELD_NAME']))
        feedback.pushInfo('OUTPUT CRS {}'.format(source.sourceCrs().authid()))
        feedback.pushInfo('AREA CRS is {}'.format(parameters['CRS_ID'].authid()))
        # If sink was not created, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSinkError method to return a standard
        # helper text for when a sink cannot be evaluated
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        # Compute the number of steps to display within the progress bar and
        # get features from source
        feature_count = source.featureCount() or 0
        total = 100.0 / feature_count if source.featureCount() else 0
        
        # Ordering by area
        request = QgsFeatureRequest()
        exp_string = f"area(transform( $geometry, '{source.sourceCrs().authid()}', '{parameters['CRS_ID'].authid()}'))"
        exp = QgsExpression(exp_string)
        clause = QgsFeatureRequest.OrderByClause(exp, ascending=parameters['ASC_DESC'])
        orderby = QgsFeatureRequest.OrderBy([clause])
        request.setOrderBy(orderby)
        features = source.getFeatures(request)

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break
            new_feature = QgsFeature(sink_fields)
            for f in source.fields():
                new_feature.setAttribute(f.name(), feature[f.name()])
            
            new_feature.setGeometry(feature.geometry())

            # Add a feature in the sink
            feat_position = f"{current}".zfill(len(str(feature_count)))
            new_feature.setAttribute(self.NEW_POSITION, current)
            new_feature.setAttribute(parameters['FIELD_NAME'], f"{parameters[self.LABEL_PREFIX]}{feat_position}{parameters[self.LABEL_SUFIX]}")

            sink.addFeature(new_feature, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))
        


        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.OUTPUT: dest_id}
